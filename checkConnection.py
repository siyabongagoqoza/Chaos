import pyttsx3 as p

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
	import requests
except:
	speak("I am missing the requests module")

url = "http://www.kite.com"
timeout = 5


def checkCONN():
	try:
		request = requests.get(url, timeout=timeout)
		print("Connected to the internet")
		conne = True
	except (requests.ConnectionError, requests.Timeout) as Exception:
		print("No internet connection.")
		conne = False
	return conne


# checkCONN()
# if checkCONN():
	# print("everything is awesome")
# else:
# 	print("valhalla")



