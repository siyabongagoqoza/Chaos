import time
import webbrowser

import pyautogui


contactList = {"Enrico": "+27614048752"}


def sendwhatmsg(name, message):
    webbrowser.open('https://web.whatsapp.com/send?phone='+contactList[name]+'&text='+message)
    time.sleep(10)
    pyautogui.press("enter")
