from darkflow.net.build import TFNet
import cv2
import sys
import os
import glob
import json

# make sure that the cwd() in the beginning is the location of the python script (so that every path makes sense)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# change directory to the one with the files to be changed
parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
parent_path = os.path.abspath(os.path.join(parent_path, os.pardir))
GT_PATH = os.path.join(parent_path, 'PycharmProjects/LP_Recognition_TheophilBuy/mAP/input', 'detection-results')
# print(GT_PATH)
os.chdir(GT_PATH)

if not os.path.exists("backup"):
  os.makedirs("backup")

options = {"pbLoad": "/home/hp/PycharmProjects/LP_Recognition_TheophilBuy/yolo-plate.pb",
           "metaLoad": "/home/hp/PycharmProjects/LP_Recognition_TheophilBuy/yolo-plate.meta",
           "gpu": 0.9}
yoloPlate = TFNet(options)
# create VOC format files
jpg_list = glob.glob('*.jpg')
if len(jpg_list) == 0:
    print("Error: no .jpg files found in detection-results")
    sys.exit()
for tmp_file in jpg_list:
    print("Processing Image: " + tmp_file)
    # print(tmp_file)
    # 1. create new file (VOC format)
    imgcv = cv2.imread(tmp_file)
    result = yoloPlate.return_predict(imgcv)
    result = str(result)
    result = result.replace("\'", "\"")
    print(result)
    with open(tmp_file.replace(".jpg", ".json"), "a") as new_f:
        new_f.write(str(result) + '\n')
    # 2. move old file (jpg format) to backup
    os.rename(tmp_file, os.path.join("backup", tmp_file))
print("Prediction completed!")
