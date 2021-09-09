import requests

try:
    url = "https://official-joke-api.appspot.com/random_joke"
    json_data = requests.get(url).json()

    arrJ = ["",""]
    arrJ[0] = json_data["setup"]
    arrJ[1] = json_data["punchline"]


    def joke():
        return arrJ
except:
    print("Jokes are not available")
