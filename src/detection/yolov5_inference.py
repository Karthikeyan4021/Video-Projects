
# src/detection/yolov5_inference.py
import torch
import cv2

class YOLOv5:
    def __init__(self, model_name='yolov5s'):
        self.model = torch.hub.load('ultralytics/yolov5', model_name, pretrained=True)

    def detect(self, frame):
        results = self.model(frame)
        return results.xyxy[0].cpu().numpy()
