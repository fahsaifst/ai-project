from ultralytics import YOLO
#from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2
import glob

def detect_helmet():
    model = YOLO('/Users/fahsaifst/Documents/cs/year3/ai-project/best.pt')
    path_files = glob.glob('detect_test/*')
    for path_file in path_files:
        results = model.predict(source=path_file, show=True)
        print("#######################")
    #print(results)
    #return results.xyxy[0]