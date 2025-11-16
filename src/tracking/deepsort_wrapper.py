
# src/tracking/deepsort_wrapper.py
# Minimal wrapper placeholder
class DeepSORT:
    def __init__(self):
        print("Init DeepSORT placeholder")

    def update(self, detections):
        # return list of (id, box)
        return [(i, det[:4]) for i, det in enumerate(detections)]
