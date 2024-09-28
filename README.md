# Vehicle Detection and Counting with yolo

This project is a Python application that uses the YOLOv10 model to detect and count different vehicle types from video footage.

## Project Structure

Here's a quick overview of the project structure:

```plaintext
your_project/
│
├── README.md                 # Project description and instructions
├── LICENSE                   # License for the project
├── .gitignore                # Files and directories to be ignored by git
├── requirements.txt          # List of dependencies for the project
├── setup.py                  # Setup script for installing the package
├── data/                     # Directory containing input data
│   ├── cars.mp4              # Input video for processing
│   └── mask.png              # Mask image for ROI
│   └── graphics.png          # Graphics to beautify the output of the code
│   └── graphics1.png         # Graphics to beautify the output of the code
│
├── outputs/                  # Directory containing the output files
│   └── output_video.avi      # Processed video with detections
│   └── vehicle_count.txt     # Text file with vehicle counts
│
├── src/                      # Source code directory
│   ├── car_counter_final.py  # Main script for running the project
│   └── sort.py               # Implementation of the SORT algorithm
│
└── models/                   # Directory for machine learning models
    └── yolov10n.pt           # YOLOv10n model file
```

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Inputs](#inputs)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [:shield: License](#License)                             kar nemikone!!!

## Introduction
This project uses a combination of YOLOv10 for object detection and the SORT algorithm for tracking vehicles across frames in a video. It also includes a mask to focus on a specific video region.

[Back to Top](#table-of-contents)

## Features
- Detects and tracks vehicles like cars, trucks, buses, motorbikes, and people.
- Counts vehicles crossing a specified line in the video.
- Saves the results, including vehicle counts, to a text file.
- Generates an output video with visual overlays and real-time counting.
- Draws bar and pie charts instantly.
- save the video

[Back to Top](#table-of-contents)

## Inputs

### Graphics
![Graphics](https://github.com/Abyaneh/car_-counter_final-edition/blob/main/graphics.png)
![Graphics2](https://github.com/Abyaneh/car_-counter_final-edition/blob/main/graphics2.png)

### Mask
![Mask](https://github.com/Abyaneh/car_-counter_final-edition/blob/main/mask.png)
#### Hint: you can use [Canva](https://www.canva.com/) for mask.

[Back to Top](#table-of-contents)

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

:dart: Results
===
The following output files are generated after running the project:

- **Processed Video:** [Download output_video.avi](https://github.com/Abyaneh/car_-counter_final-edition/blob/main/output_video.avi)
- **Vehicle Count:** [Download vehicle_count.txt](https://github.com/Abyaneh/car_-counter_final-edition/blob/main/vehicle_count.txt)


  
### Sample of outputs

#### video output
![video_output](https://github.com/Abyaneh/car_-counter_final-edition/blob/main/sample%20of%20outputs/Sample%20video%20output.png)

#### chart output
![chart_output](https://github.com/Abyaneh/car_-counter_final-edition/blob/main/sample%20of%20outputs/Sample%20chart%20output.png)

[Back to Top](#table-of-contents)

## Contributing

We welcome contributions to this project! To contribute, please follow these guidelines:

1. **Fork the Repository**: Click on the 'Fork' button at the top of this repository page to create a copy of the repository in your GitHub account.



2. **Clone the Forked Repository**: Clone the forked repository to your local machine using the following command:
    ```bash
    git clone https://github.com/your-username/your_project.git
    ```


3. **Create a New Branch**: Create a new branch to work on your changes:
    ```bash
    git checkout -b feature/your-feature-name
    ```



4. **Make Your Changes**: Make your changes or additions to the codebase.

5. **Test Your Changes**: Ensure that your changes do not break any existing functionality. Add tests if necessary.


6. **Commit Your Changes**: Commit your changes with a descriptive commit message:
    ```bash
    git commit -m "Add feature: description of your feature"
    ```

7. **Push to Your Fork**: Push your changes to your forked repository:
    ```bash
    git push origin feature/your-feature-name
    ```

8. **Submit a Pull Request**: Go to the original repository on GitHub and submit a pull request. Please include a detailed description of your changes and the issue you are addressing.


9. **Review Process**: The project maintainers will review Your pull request. Feedback may be provided so you can make the necessary revisions.


### Reporting Issues

If you find any bugs or issues in the project, please create an issue in the [Issues](https://github.com/Abyaneh/car_-counter_final-edition/issues) section of the repository with a detailed description of the problem and steps to reproduce it.

Thank you for your contributions!

[Back to Top](#table-of-contents)

:shield: License
===
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Abyaneh/car_-counter_final-edition/blob/main/LICENSE.txt) file for details.

[Back to Top](#table-of-contents)
