import datetime
# import cv2
#
#
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#
# if not(cap.isOpened()):
#     print("could not open cam")
#
# print(datetime.date.today() + datetime.timedelta(days=1))
text2 = "text hello to Siya"
infoSrch = text2.split()
infoSrch.remove("text")
sIndex = infoSrch.index("to")
fullMsg = infoSrch[::sIndex]
# whatppname = infoSrch[sIndex::]
# print(whatppname)
print(fullMsg)