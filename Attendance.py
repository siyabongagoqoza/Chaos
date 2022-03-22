import pyttsx3 as p
from installMissingModules import *
# registering text to speech module FIRST
engine = p.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 127)
voices = engine.getProperty('voices')


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


import getpass
import time
import datetime
try:
    import cv2
except:
    speak("I am missing the opencv-python module")
    install("opencv-python")
import numpy as np
try:
    import face_recognition
except:
    speak("I maybe missing the face_recognition, dlib and cmake modules")
    install("cmake")
    install("dlib")
    install("face_recognition")
import os

userAccount = getpass.getuser()

path = "C:\\Users\\"+userAccount+"\\CHAOS\\imagesAttendance"
images = []
classNames = []
myList = os.listdir(path)
# print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
# print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


encodeListKnown = findEncodings(images)
# print(len(encodeListKnown))
speak("Identify yourself")

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# id timer verification
timeoutID = time.time() + 5  # 5 seconds

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        # print(faceDis)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
    try:
        if not(name is None):
            print(name + " Identified")
            break
        if name is None:
            speak("You don't have permission Authorization")
            continue
    except:
        pass

    # cv2.imshow("webcam", img)
    # cv2.waitKey(1)

greetingTime = datetime.datetime.now()

if name == "SIYABONGA GOQOZA":

    if 00 <= int(greetingTime.strftime("%H")) <= 11:
        speak("Good Morning Sir")

    if 12 <= int(greetingTime.strftime("%H")) <= 16:
        speak("Good afternoon Sir")

    if 17 <= int(greetingTime.strftime("%H")) <= 23:
        speak("Good Evening Sir")

elif name == "ENRICO SAMUELS":
    if 00 <= int(greetingTime.strftime("%H")) <= 11:
        speak("Good Morning Enrico")

    if 12 <= int(greetingTime.strftime("%H")) <= 16:
        speak("Good afternoon Enrico")

    if 17 <= int(greetingTime.strftime("%H")) <= 23:
        speak("Good Evening Enrico")





