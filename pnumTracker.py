from installMissingModules import *
import pyttsx3 as p

# registering text to speech module FIRST

engine = p.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', 127)
voices = engine.getProperty('voices')


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


import os
import random
try:
    import phonenumbers
except:
    speak("I am missing the phonenumbers module")
    install("phonenumbers")

try:
    import ipinfo
except:
    speak("I am missing the ipinfo module")
    install("ipinfo")
import socket


# getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
# getting the IP address using socket.gethostbyname() method
ipaddress = socket.gethostbyname(hostname)
print(ipaddress)
access_token = '796fe59bdb5709'
handler = ipinfo.getHandler(access_token)
ip_address = ipaddress
details = handler.getDetails(ipaddress)
print(details.city)
from phonenumbers import geocoder

# ch_number = phonenumbers.parse('+27614048752', "CH")
# print(geocoder.description_for_number(ch_number, "en"))
# from phonenumbers import carrier
# service_provider = phonenumbers.parse('+27614048752', "RO")
# print(carrier.name_for_number(service_provider, "en"))
