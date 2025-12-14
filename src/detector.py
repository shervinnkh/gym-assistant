import cv2
from src.utils import getRotation
from ultralytics import YOLO
from numpy import argmax


def loadModel(modelIndex):
    downloadedYoloModels = ["yolov8n-pose.pt","yolov8m-pose.pt"]
    model = YOLO('./models/'+downloadedYoloModels[modelIndex])
    return model
 
def assist(exercise,results,imagef):
    index = argmax( results[0].boxes.conf.tolist())
    index =index.item()
    keys =results[0].keypoints[index]
    detected = keys.has_visible
    confs = keys.conf.tolist()[0]
    pointsXY = keys.xyn.tolist()[0]
    pointsMainXY = keys.xy.tolist()[0]

    isRight,detected = getRotation(confs)

    exercise.defineRightLeft(isRight)

    
    OK = exercise.check(pointsXY,confs)


    if(exercise.twoSide):
        exercise.defineDrawChecks(exercise.rightChecks)
        
        img = exercise.draw_all_actions(imagef,OK,pointsMainXY)

        exercise.defineDrawChecks(exercise.leftChecks)
        img = exercise.draw_all_actions(img,OK,pointsMainXY)
    else:
        exercise.defineDrawChecks(exercise.checks)
        img = exercise.draw_all_actions(imagef,OK,pointsMainXY)
    
    
    col = (0,255,0)
    text = "Correct"
    if(OK==False):
        col = (0,0,255)
        text = "Incorrect"

    #Write reuslt
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 3
    thickness = 5
    x = int(img.shape[1] / 2 ) -150
    y = 600
    _=cv2.putText(img, text, (x, y), font, fontScale, (0,0,0), thickness + 2, lineType=cv2.LINE_AA)
    out=cv2.putText(img, text, (x, y), font, fontScale, col, thickness, lineType=cv2.LINE_AA)

    return out
    
def posProcess (model , exercise ,frame):
    results = model(frame)
    if(len(results[0].boxes.conf.tolist()) > 0):
        img = assist(exercise,results,frame)
        return img , True
    else :
        return None , False