import getpass
import os

import pyttsx3 as p
from installMissingModules import *
# registering text to speech module FIRST
engine = p.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


try:
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
except:
    speak("I am missing the pydrive module")
    install("pydrive")
import shutil
from shutil import make_archive


userAccount = getpass.getuser()
print(userAccount)

client_json_path = 'C:\\Users\\'+userAccount+'\\PycharmProjects\\Chaos\\uploadToCloud\\client_secrets.json'
GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = client_json_path
gauth = GoogleAuth()
drive = GoogleDrive(gauth)


# Save my credentials for the first time to speed up authentication
def saveCreds():

    # Try to load saved client credentials
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there
        speak("Sir I will need your manual authentication")
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
    # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")


# zips save game folders
def zip_minecraft_naruto():
    # get the path to the files
    srcMinecraft = os.path.realpath('C:\\Users\\'+userAccount+'\\AppData\\Roaming\\.minecraft\\'
                                    'versions\\RLCraft 1.12.2 - Beta v2.8.2\\saves\\Chaos Dimension')
    srcNarutoSS = os.path.realpath('C:\\Users\\' + userAccount + '\\Saved Games\\NARUTO TO BORUTO SHINOBI STRIKER')
    # put things into ZIP archive
    root_dir, tail = os.path.split(srcMinecraft)
    shutil.make_archive("Chaos Dimension", "zip", root_dir)
    root_dir2, tail = os.path.split(srcNarutoSS)
    shutil.make_archive("NarutoSS", "zip", root_dir2)


# uploads save game zip files to google drive
def upload_to_drive():
    saveCreds()
    zip_minecraft_naruto()  # Zips the file
    upload_file_list = ['Chaos Dimension.zip', 'NarutoSS.zip']
    for upload_file in upload_file_list:
        gfile = drive.CreateFile({'parents': [{'id': '1cPAp2_tREoJVmYJxEYKTjGTnUqActJt2'}]})
        # Read file and set it as the content of this instance.
        gfile.SetContentFile(upload_file)
        gfile.Upload()  # upload the file

    speak("The files have been stored in the cloud")


# upload_to_drive()
