# Vehicle Detection and Counting with yolo

This project is a Python application that uses the YOLOv10 model to detect and count different vehicle types from video footage.

## Project Structure

Here's a quick overview of the project structure:

```plaintext
your_project/
│
├── README.md               # Project description and instructions
├── LICENSE                 # License for the project
├── .gitignore              # Files and directories to be ignored by git
├── requirements.txt        # List of dependencies for the project
├── setup.py                # Setup script for installing the package
├── data/                   # Directory containing input data
│   ├── cars.mp4            # Input video for processing
│   └── mask.png            # Mask image for ROI
│
├── outputs/                # Directory containing the output files
│   └── output_video.avi    # Processed video with detections
│   └── vehicle_count.txt   # Text file with vehicle counts
│
├── src/                    # Source code directory
│   ├── main.py             # Main script for running the project
│   └── sort.py             # Implementation of the SORT algorithm
│
└── models/                 # Directory for machine learning models
    └── yolov10n.pt         # YOLOv10n model file
```

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project uses a combination of YOLOv10 for object detection and the SORT algorithm for tracking vehicles across frames in a video. It also includes a mask to focus on a specific video region.

## Features
- Detects and tracks vehicles like cars, trucks, buses, motorbikes, and people.
- Counts vehicles crossing a specified line in the video.
- Saves the results, including vehicle counts, to a text file.
- Generates an output video with visual overlays and real-time counting.
- save the video

## Input Data

![Graphics](https://github.com/Abyaneh/car_-counter_final-edition/blob/main/graphics.png)

![Mask](https://github.com/Abyaneh/car_-counter_final-edition/blob/main/mask.png)



## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your_project.git
    cd your_project
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download the YOLOv10 model weights and place them in the `models/` directory.

## Usage

To run the vehicle detection and counting script, use the following command:

```bash
python src/main.py

git add output_video.avi vehicle_count.txt
git commit -m "Add output video and vehicle count files"
git push origin main
```




### 2. **افزودن فایل‌های Outputs به README.md**

برای فایل‌های `output_video.avi` و `vehicle_count.txt` که در پوشه `outputs/` قرار دارند، اگر نمی‌خواهید آن‌ها را در مخزن اصلی ذخیره کنید، می‌توانید به روش‌های زیر عمل کنید:

#### الف) **اشتراک‌گذاری لینک‌های دانلود فایل‌های خروجی**

اگر فایل‌های `output_video.avi` و `vehicle_count.txt` را در GitHub Releases آپلود کرده‌اید، می‌توانید لینک‌های دانلود آن‌ها را در README.md قرار دهید.

```markdown
## Output Files

The following output files are generated after running the project:

- **Processed Video:** [Download output_video.avi](https://github.com/yourusername/yourrepo/releases/download/v1.0/output_video.avi)
- **Vehicle Count:** [Download vehicle_count.txt](https://github.com/yourusername/yourrepo/releases/download/v1.0/vehicle_count.txt)
```



## Output:

[Download output_video.avi](https://github.com/Abyaneh/car_-counter_final-edition/blob/main/output_video.avi)


