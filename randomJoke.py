import requests

try:
    joke_validate = ""
    url = "https://v2.jokeapi.dev/joke/Any?type=twopart&safemode"
    json_data = requests.get(url).json()

    arrJ = ["",""]
    arrJ[0] = json_data["setup"]
    arrJ[1] = json_data["delivery"]


    def joke():
        return arrJ
except:
    joke_validate = "Jokes are not available"
