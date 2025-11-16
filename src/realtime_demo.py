
# src/realtime_demo.py
import cv2
from detection.yolov5_inference import YOLOv5
from tracking.deepsort_wrapper import DeepSORT

def run():
    det = YOLOv5()
    tracker = DeepSORT()
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret: break
        boxes = det.detect(frame)
        tracked = tracker.update(boxes)
        for tid, box in tracked:
            x1,y1,x2,y2 = map(int, box)
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.putText(frame,f"ID:{tid}",(x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
        cv2.imshow("Video",frame)
        if cv2.waitKey(1)&0xFF==ord('q'): break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run()
