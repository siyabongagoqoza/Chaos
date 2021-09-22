import getpass
import time

import cv2
import numpy as np
import face_recognition
import os

userAccount = getpass.getuser()
path = "C:\\Users\\"+userAccount+"\\PycharmProjects\\CHAOS\\imagesAttendance"
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
print("Encode Complete")

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# id timer verification
timeoutID = time.time() + 4

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
    except:
        pass

    # cv2.imshow("webcam", img)
    # cv2.waitKey(1)






