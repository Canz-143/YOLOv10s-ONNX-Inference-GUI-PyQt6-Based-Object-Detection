# YOLOv10s ONNX Inference GUI

## Overview
This repository contains a PyQt6-based GUI application for performing object detection inference using a YOLOv10s model in ONNX format. The application allows users to load a trained model, select an image or video, and visualize inference results in real-time.

The dataset used to train the model is purely synthetic, generated using Blender and Unity with the Unity Perception package for controlled dataset creation. This ensures high-quality labeled data for training.

## Features
- **Graphical User Interface (GUI):** Built using PyQt6, providing an intuitive interface for model selection and inference.
- **ONNX Model Support:** Runs inference using a YOLOv10s model trained on synthetic data.
- **Image and Video Inference:** Supports processing both image and video files.
- **Real-time Visualization:** Displays annotated frames in a window for easy monitoring.
- **Synthetic Data Pipeline:** The training data was generated using Blender and Unity, allowing precise object placement and labeling.

## Dependencies
Ensure you have the following dependencies installed:
```sh
pip install torch torchvision numpy opencv-python PyQt6 ultralytics
```

## Installation
Clone this repository and navigate to the directory:
```sh
git clone https://github.com/yourusername/YOLOv10s-Inference-GUI.git
cd YOLOv10s-Inference-GUI
```

## Usage
1. **Run the Application:**
   ```sh
   python main.py
   ```
2. **Load the YOLOv10s ONNX model** by clicking the "Select ONNX Model" button.
3. **Select an Image or Video File** for inference.
4. Click **"Run Inference"** to start processing.
5. View the results in an OpenCV window. Press 'q' to exit video inference mode.

## File Structure
```
YOLOv10s-Inference-GUI/
│── main.py               # Main script for the GUI and inference logic
│── README.md             # Project documentation
│── requirements.txt      # List of dependencies
```

## Model Details
- **Model Used:** YOLOv10s (ONNX format)
- **Training Pipeline:**
  - **Synthetic Data:** Generated using Blender and Unity Perception package.
  - **Data Augmentation:** Applied through Unity’s Perception tools.
  - **Training Framework:** Trained using Ultralytics YOLO.

## Notes
- Ensure that your ONNX model is compatible with YOLO inference.
- The application currently does not support live webcam inference (but can be extended).

## Future Improvements
- Add support for live webcam inference.
- Implement multi-threaded video processing for better performance.
- Improve UI for real-time frame display.

## License
This project is licensed under the MIT License.

## Acknowledgments
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- [Unity Perception Package](https://github.com/Unity-Technologies/com.unity.perception)