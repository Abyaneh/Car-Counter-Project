# library:

from ultralytics import YOLO
import cv2
import cvzone
import math
from sort import Sort
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

def initialize_video_and_model(video_path, model_path):
    """
    Initialize video capture and YOLO model.
    
    Parameters:
        video_path (str): Path to the video file.
        model_path (str): Path to the YOLO model weights.
    
    Returns:
        cap: VideoCapture object.
        model: YOLO model object.
    """
    cap = cv2.VideoCapture(video_path)
    model = YOLO(model_path)
    return cap, model

def load_image(file_path, check_channels=True, alpha=False):
    """
    Load an image from file and optionally check its channels.
    
    Parameters:
        file_path (str): Path to the image file.
        check_channels (bool): Whether to check the number of channels in the image.
        alpha (bool): Whether the image should have an alpha channel.
    
    Returns:
        img: Loaded image as a numpy array.
    
    Raises:
        FileNotFoundError: If the image file is not found.
        ValueError: If the image doesn't have the expected number of channels.
    """
    img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise FileNotFoundError(f"Image file not found: {file_path}")
    if check_channels:
        if alpha and img.shape[2] != 4:
            raise ValueError(f"Image {file_path} must have 4 channels (RGBA).")
        elif not alpha and img.shape[2] != 3:
            raise ValueError(f"Image {file_path} must have 3 channels (RGB).")
    return img

def preprocess_frame(frame, mask):
    """
    Apply a mask to the frame.
    
    Parameters:
        frame (numpy.ndarray): Video frame.
        mask (numpy.ndarray): Mask image.
    
    Returns:
        numpy.ndarray: Masked frame.
    
    Raises:
        ValueError: If the mask and frame have different numbers of channels.
    """
    if len(mask.shape) == 2:  # If mask is single channel (grayscale)
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)  # Convert single channel mask to 3 channels (BGR)
    elif mask.shape[2] == 4:  # If mask has 4 channels (RGBA)
        mask = cv2.cvtColor(mask, cv2.COLOR_BGRA2BGR)  # Convert RGBA to BGR (remove alpha channel)
    
    if frame.shape[2] != mask.shape[2]:
        raise ValueError("Mask image must have the same number of channels as the video frame.")
    
    mask_resized = cv2.resize(mask, (frame.shape[1], frame.shape[0]))
    return cv2.bitwise_and(frame, mask_resized)

def draw_vehicle_counts(img, vehicle_count):
    """
    Draw the vehicle counts on the image.
    
    Parameters:
        img (numpy.ndarray): The image where the counts will be drawn.
        vehicle_count (dict): Dictionary with vehicle types and their counts.
    """
    y_offset = 200
    for vehicle_type, count in vehicle_count.items():
        cv2.putText(img, f'{vehicle_type}: {count}', (50, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        y_offset += 50

def update_plot(vehicle_count):
    """
    Update and display live plots for vehicle counts.
    
    Parameters:
        vehicle_count (dict): Dictionary with vehicle types and their counts.
    """
    plt.clf()
    vehicle_types = list(vehicle_count.keys())
    vehicle_counts = list(vehicle_count.values())

    # Bar chart
    plt.subplot(1, 2, 1)
    plt.bar(vehicle_types, vehicle_counts, color=['blue', 'green', 'red', 'orange'])
    plt.title('Vehicle Type Counts')
    plt.xlabel('Vehicle Type')
    plt.ylabel('Count')

    # Pie chart
    plt.subplot(1, 2, 2)
    colors = ['b', 'g', 'r', 'orange']
    plt.pie(vehicle_counts, labels=vehicle_types, colors=colors, autopct='%1.1f%%')
    plt.title('Vehicle Type Distribution')

    plt.draw()
    plt.pause(0.0001)

def process_video(cap, model, mask, tracker, limits, tracked_classes, out_video):
    """
    Process video to detect and track vehicles.
    
    Parameters:
        cap: VideoCapture object.
        model: YOLO model object.
        mask (numpy.ndarray): Mask image.
        tracker: SORT tracker object.
        limits (list): List of line coordinates for counting vehicles.
        tracked_classes (list): List of vehicle classes to track.
        out_video: VideoWriter object to save the output video.
    
    Returns:
        total_count (list): List of all tracked vehicle IDs.
        vehicle_count (dict): Dictionary with vehicle types and their counts.
    """
    total_count = []
    vehicle_count = defaultdict(int)

    plt.ion()  # Turn on interactive mode for live updates

    while True:
        success, img = cap.read()
        if not success:
            break

        img_region = preprocess_frame(img, mask)
        img_graphics = load_image('graphics.png', check_channels=False, alpha=True)
        if img_graphics.shape[2] == 3:  # If the image does not have alpha channel, add it
            img_graphics = cv2.merge([img_graphics, np.ones((img_graphics.shape[0], img_graphics.shape[1]), dtype=np.uint8) * 255])
        cvzone.overlayPNG(img, img_graphics, (0, 0))

        results = model(img_region, stream=True)
        detections = np.empty((0, 5))

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                conf = math.ceil(box.conf[0] * 100) / 100
                cls = int(box.cls[0])
                current_class = class_names[cls]

                if current_class in tracked_classes and conf > 0.3:
                    current_array = np.array([x1, y1, x2, y2, conf])
                    detections = np.vstack((detections, current_array))

        results_tracker = tracker.update(detections)

        cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 0, 255), 5)
        for result in results_tracker:
            x1, y1, x2, y2, id = result
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            cvzone.cornerRect(img, (x1, y1, w, h), l=9, rt=5, colorR=(255, 0, 255))
            cvzone.putTextRect(img, f'{int(id)}', (max(0, x1), max(35, y1)), scale=2, thickness=3, offset=10)
            cx, cy = x1 + w // 2, y1 + h // 2
            cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            if limits[0] < cx < limits[2] and limits[1] - 15 < cy < limits[3] + 15:
                if id not in total_count:
                    total_count.append(id)
                    vehicle_count[current_class] += 1
                    cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), (0, 255, 0), 5)

                    update_plot(vehicle_count)

        # Draw vehicle counts on the image
        draw_vehicle_counts(img, vehicle_count)
        cv2.putText(img, str(len(total_count)), (255, 100), cv2.FONT_HERSHEY_PLAIN, 5, (50, 50, 255), 8)
        cv2.imshow('Image', img)

        # Write the frame to the output video
        out_video.write(img)

        # Handling keyboard inputs for interactive video processing
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('d'):
            cap.set(cv2.CAP_PROP_POS_MSEC, cap.get(cv2.CAP_PROP_POS_MSEC) + 30000)  # Skip forward 30 seconds
        elif key == ord('a'):
            cap.set(cv2.CAP_PROP_POS_MSEC, max(0, cap.get(cv2.CAP_PROP_POS_MSEC) - 10000))  # Rewind10 seconds

    plt.ioff()  # Turn off interactive mode after processing
    plt.show()
    return total_count, vehicle_count

def save_results(total_count, vehicle_count):
    """
    Save vehicle count results to a text file.
    
    Parameters:
        total_count (list): List of all tracked vehicle IDs.
        vehicle_count (dict): Dictionary with vehicle types and their counts.
    """
    total_vehicle_count = len(total_count)
    with open("vehicle_count.txt", "w") as file:
        file.write("Vehicle Count Summary:\n")
        for vehicle_type, count in vehicle_count.items():
            percentage = (count / total_vehicle_count) * 100 if total_vehicle_count > 0 else 0
            file.write(f"{vehicle_type}: {count} ({percentage:.2f}%)\n")
        file.write(f"\nTotal Vehicles: {total_vehicle_count}")

if __name__ == "__main__":
    # List of COCO class names
    class_names = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
                   "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
                   "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
                   "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
                   "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
                   "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
                   "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
                   "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
                   "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
                   "teddy bear", "hair drier", "toothbrush"]

    tracked_classes = ["person", "car", "bus", "truck", "motorbike"]
    mask = load_image("mask.png", check_channels=False)  # Load mask image
    tracker = Sort(max_age=20, min_hits=3, iou_threshold=0.3)  # Initialize SORT tracker
    limits = [400, 297, 673, 297]  # Define counting line coordinates

    # Initialize video capture and YOLO model
    cap, model = initialize_video_and_model('cars.mp4', '../Yolo-Weights/yolov10x')

    # Setup video writer for output video
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out_video = cv2.VideoWriter('output_video.avi', cv2.VideoWriter_fourcc(*'XVID'), 30, (frame_width, frame_height))

    # Process the video to detect and track vehicles
    total_count, vehicle_count = process_video(cap, model, mask, tracker, limits, tracked_classes, out_video)
    
    # Save the results to a text file
    save_results(total_count, vehicle_count)

    # Release the video capture object and video writer
    cap.release()
    out_video.release()
    cv2.destroyAllWindows()
