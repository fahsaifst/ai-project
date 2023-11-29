import cv2
import argparse
import tensorflow as tf
import serial

import supervision as sv 
from ultralytics import yolov8 as YOLO

from pydub import AudioSegment
from pydub.playback import play

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='YOLOv8 Object Detection')
    parser.add_argument(
         "--webcam-resolution",
         defult=[1280, 720],
         type=int,
         nargs=2,)
    args = parser.parse_args()
    return args

# เขียนตรงนี้จ้า
def main(frame):
    classes = ['helmet', 'no_helmet'] # [0, 1]

    args = parse_args()
    frame_width = args.webcam_resolution[0]
    frame_height = args.webcam_resolution[1]

    model = YOLO('best.pt')

    box_annotation = sv.BoxAnnotation(
        thickness=2,
        text_size=1.0,
        text_thickness=2,
    )

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

    while True:
        ret, frame = cap.read()
        result = model(frame)[]
        detections = sv.Detection.from_yolov8(result)
        lables = [
            f'{model.model.names[class_id]} {confidence:0.2f}'
            for _, confidence, class_id, 
            in detections
        ]
        frame = box_annotation.annotate(
            scene = frame, 
            detections = detections,
            lables = lables
        )
       if lables == 'no_helmet':
       # cv2.imshow('not_helmet', frame)

        if not ret:
            break
        no_helmet_detected = main(frame)

        if any(class_id == 1 for _, _, class_id, _ in detections):
            detected_class = "no_helmet"
            print("Warning! Rider or passenger doesn't wearing HELMET!")
            print("Detected Class: ", detected_class)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
