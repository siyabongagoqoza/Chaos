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
# Function to convert
def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele + " "

        # return string
    return str1

liste = ['a','e','d','f','g']
print(listToString(liste))
