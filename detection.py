from ultralytics import YOLO
#from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2
import glob

def detect_helmet():
    model = YOLO('/Users/fahsaifst/Desktop/ultralytics/model/best_v9.pt') #lastest model is best_v9
    path_files = glob.glob('detect_test/*')
    for path_file in path_files:
        #source from imgs and videos folder
        #results = model.predict(source=path_file, show=True)
        
        #source from partucular img and video folder
        results = model.predict(source='', show=True)
        
        #source from default webcam
        results = model.predict(source="0", show=True)
        
        print("#######################")
    #print(results)
    #return results.xyxy[0]