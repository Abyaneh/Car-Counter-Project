# Vehicle Detection and Counting with yolo

This project is a Python application that uses the YOLOv10 model to detect and count different vehicle types from video footage.

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




## Results

The processed video with detections and tracking can be viewed here:
[output_video.avi](https://github.com/Abyaneh/car_-counter_final-edition/blob/main/output_video.avi)

The vehicle count results can be found here:
[vehicle_count.txt](https://github.com/Abyaneh/car_-counter_final-edition/blob/main/vehicle_count.txt)










### 3. **فایل LICENSE**
لایسنس استفاده از کد را مشخص می‌کند. یکی از لایسنس‌های محبوب، MIT License است:

```plaintext
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

