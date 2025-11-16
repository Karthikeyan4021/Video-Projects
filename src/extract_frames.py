
# src/extract_frames.py
import cv2
import os

def extract(video_path, out_dir, fps=5):
    os.makedirs(out_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    count = 0
    idx = 0
    orig_fps = cap.get(cv2.CAP_PROP_FPS)
    step = int(orig_fps / fps) if orig_fps>0 else 1
    while True:
        ret, frame = cap.read()
        if not ret: break
        if count % step == 0:
            cv2.imwrite(os.path.join(out_dir, f"frame_{idx:06d}.jpg"), frame)
            idx+=1
        count+=1
    cap.release()

if __name__ == "__main__":
    print("Usage: extract('video.mp4','frames',fps=5)")
