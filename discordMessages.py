import json

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


try:
    import websocket
except:
    speak("I am missing the websocket-client module")
    install('websocket-client')


def send_json_request(ws, request):
    ws.send(json.dumps(request))


def receive_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)


ws = websocket.WebSocket()
ws.connect("wss://gateway.discord.gg/?v=6&encording=json")
heartbeat_interval = receive_json_response(ws)["d"]["heartbeat_interval"]

token = "Njk0NDg2MDE2MDE0NDE3OTcw.YV1slQ.j89l72A5PD8eW6CDrRbwrCJUAfE"
payload = {
    "op": 2,
    "d": {
        "token": token,
        "intents": 513,
        "properties": {
            "$os": "windows",
            "$browser": "chrome",
            "$device": "pc"
        }
    }
}
send_json_request(ws, payload)

while True:
    event = receive_json_response(ws)
    try:
        content = event['d']['content']
        author = event['d']['author']['username']
        print(f'{author}: {content}')
    except:
        pass
