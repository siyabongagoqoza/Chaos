import cv2
import numpy as np
import face_recognition

imgSiya = face_recognition.load_image_file("imagesBasic/newFile-2.jpg")
imgSiya = cv2.cvtColor(imgSiya, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file("imagesBasic/Johnny Depp2.jpg")
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgSiya)[0]
encodeSiya = face_recognition.face_encodings(imgSiya)[0]
cv2.rectangle(imgSiya, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0,255,0), 2)
print(faceLoc)

faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest= face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (0, 255, 0), 2)

results = face_recognition.compare_faces([encodeSiya],encodeTest)
faceDis = face_recognition.face_distance([encodeSiya],encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0],2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255), 2)

cv2.imshow("Siya", imgSiya)
cv2.imshow("Siya Test", imgTest)
cv2.waitKey(0)
