import getpass
import glob
import os

userAccount = getpass.getuser()
os.chdir("C:\\Users\\" + userAccount + "\\MyApps")

addToDict = {}


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele + " "

        # return string
    return str1


def scanFiles():
    for file in glob.glob("*.lnk"):
        fileLocal = "C:\\Users\\" + userAccount + "\\MyApps" + "\\" + file
        fileName = file.replace(".lnk", "")
        #print(fileName)
        addToDict[fileName] = fileLocal


def find_files(filename):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk("C:\\Program Files (x86)"):
      if filename in files:
         result.append(os.path.join(root, filename))
   for root, dir, files in os.walk("C:\\Program Files"):
      if filename in files:
         result.append(os.path.join(root, filename))

   print(result)
   return result


# os.startfile(listToString(find_files('.exe')))

#print(addToDict)


