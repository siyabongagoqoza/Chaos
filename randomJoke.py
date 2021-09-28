import requests

try:
    joke_validate = ""


    def getJoke():

        url = "https://v2.jokeapi.dev/joke/Any?type=twopart&safemode"
        json_data = requests.get(url).json()

        arrJ = ["",""]
        arrJ[0] = json_data["setup"]
        arrJ[1] = json_data["delivery"]
        return arrJ

except:
    joke_validate = "Jokes are not available"
