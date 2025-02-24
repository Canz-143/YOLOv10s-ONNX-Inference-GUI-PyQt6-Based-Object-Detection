import sys
import cv2
import torch
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QVBoxLayout
from PyQt6.QtGui import QPixmap, QImage
from ultralytics import YOLO

class YOLOInferenceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.model = None
        self.video_path = None
        self.image_path = None

    def initUI(self):
        self.setWindowTitle("YOLOv10 ONNX Inference")
        self.setGeometry(100, 100, 500, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Select a model, video, or image to start inference", self)
        layout.addWidget(self.label)

        self.modelButton = QPushButton("Select ONNX Model", self)
        self.modelButton.clicked.connect(self.load_model)
        layout.addWidget(self.modelButton)

        self.videoButton = QPushButton("Select Video", self)
        self.videoButton.clicked.connect(self.load_video)
        layout.addWidget(self.videoButton)

        self.imageButton = QPushButton("Select Image", self)
        self.imageButton.clicked.connect(self.load_image)
        layout.addWidget(self.imageButton)

        self.inferButton = QPushButton("Run Inference", self)
        self.inferButton.clicked.connect(self.run_inference)
        layout.addWidget(self.inferButton)
        self.inferButton.setEnabled(False)

        self.setLayout(layout)

    def load_model(self):
        model_path, _ = QFileDialog.getOpenFileName(self, "Select ONNX Model", "", "ONNX Files (*.onnx)")
        if model_path:
            self.model = YOLO(model_path)
            self.label.setText(f"Model Loaded: {model_path}")
            self.check_ready()

    def load_video(self):
        video_path, _ = QFileDialog.getOpenFileName(self, "Select Video File", "", "Video Files (*.mp4 *.avi *.mov)")
        if video_path:
            self.video_path = video_path
            self.label.setText(f"Video Loaded: {video_path}")
            self.check_ready()

    def load_image(self):
        image_path, _ = QFileDialog.getOpenFileName(self, "Select Image File", "", "Image Files (*.jpg *.jpeg *.png)")
        if image_path:
            self.image_path = image_path
            self.label.setText(f"Image Loaded: {image_path}")
            self.check_ready()

    def check_ready(self):
        if self.model and (self.video_path or self.image_path):
            self.inferButton.setEnabled(True)

    def run_inference(self):
        if not self.model or not (self.video_path or self.image_path):
            return

        if self.video_path:
            cap = cv2.VideoCapture(self.video_path)
            if not cap.isOpened():
                self.label.setText("Error opening video file")
                return

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break

                results = self.model(frame)
                annotated_frame = results[0].plot()

                cv2.imshow("YOLOv8 Inference", annotated_frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cap.release()
            cv2.destroyAllWindows()

        elif self.image_path:
            image = cv2.imread(self.image_path)
            results = self.model(image)
            annotated_image = results[0].plot()

            cv2.imshow("YOLOv8 Inference", annotated_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = YOLOInferenceApp()
    window.show()
    sys.exit(app.exec())
