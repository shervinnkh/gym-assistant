from src.exercises import exercises
from src.detector import loadModel, assist, posProcess
import cv2

def __main__():

    model = loadModel(0)

    exercise = exercises[1]

    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        outPutImage,hasData = posProcess(model,exercise,frame)
        if(hasData):
            cv2.imshow("GYMAssistent", outPutImage)
        if cv2.waitKey(1) & 0xFF == 27: 
            break


    cap.release()
    cv2.destroyAllWindows()


__main__()