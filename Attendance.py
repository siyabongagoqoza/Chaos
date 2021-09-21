import cv2
import numpy as np
import face_recognition
import os

path = "imagesAttendance"
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


imgSiya = face_recognition.load_image_file("imagesBasic/newFile-2.jpg")
imgSiya = cv2.cvtColor(imgSiya, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file("imagesBasic/Johnny Depp2.jpg")
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
