import glob
import os

os.chdir("C:\\Users\\Siyabonga Goqoza\\MyApps")

addToDict = {}


def scanFiles():
    for file in glob.glob("*.lnk"):
        fileLocal = "C:\\Users\\Siyabonga Goqoza\\MyApps" + "\\" + file
        fileName = file.replace(".lnk", "")
        #print(fileName)
        addToDict[fileName] = fileLocal




#print(addToDict)


