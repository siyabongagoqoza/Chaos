import getpass
import glob
import os

userAccount = getpass.getuser()
os.chdir("C:\\Users\\" + userAccount + "\\MyApps")

addToDict = {}


def scanFiles():
    for file in glob.glob("*.lnk"):
        fileLocal = "C:\\Users\\" + userAccount + "\\MyApps" + "\\" + file
        fileName = file.replace(".lnk", "")
        #print(fileName)
        addToDict[fileName] = fileLocal




#print(addToDict)


