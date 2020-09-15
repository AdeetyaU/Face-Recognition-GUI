import cv2
import os
import pandas as pd
def initialize():
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel" + os.sep + "Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("StudentDetails" + os.sep + "StudentDetails.csv")
    font = cv2.FONT_HERSHEY_SIMPLEX
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height
    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    return faceCascade,recognizer,df,minW,minH,font,cam

def cam(faceCascade,recognizer,df,minW,minH,font,cam):
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5, minSize=(int(minW), int(minH)), flags=cv2.CASCADE_SCALE_IMAGE)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (10, 159, 255), 2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])

            if conf < 100:
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
            else:
                tt = ''

            tt = str(tt)[2:-2]
            if (100 - conf) > 50:
                cv2.putText(im, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        return im
