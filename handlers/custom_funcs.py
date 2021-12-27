import math

import json
from flask.json import jsonify
import requests
def callLaps():
    res = requests.get("http://es2.assettohosting.com:10339/results/download/211225_224016_FP.json")
    # Convert data to dict
    TT = json.loads(res.text)
    PILOTO = extractPilots(TT)
    for driver in PILOTO:
        extractLaps(driver["carId"], json.loads(res.text))
    vueltasa:list = []
    # return jsonify({"piloto": PILOTO})
    return TT

    # Convert dict to string
def extractLaps(carId,jsonObj: dict):
    for element in jsonObj["laps"]:
        if (str(element["carId"])==carId) & element["isValidForBest"] == True:
            print("===laaptime id " + carId)
            print(element["laptime"])

def extractPilots(jsonObj: dict):
    pilotos:list = [];
    for element in jsonObj["sessionResult"]["leaderBoardLines"]:
        print(element["car"]["carId"])
        pilotos.append({"carId": str(element["car"]["carId"]),"piloto":str(element["car"]["drivers"][0]['firstName'] + " " + element["car"]["drivers"][0]['lastName'])})
    return pilotos
def switch_statement(arg: str):
    if arg == "png":
        return 1
    if arg == "jpg":
        return 2
    if arg == "jpeg":
        return 3
    if arg == "tiff":
        return 4
    if arg == "bmp":
        return 5
    else:
        return 0
def lapTime(duration: int):
    milliseconds  = int((duration % 1000) / 1)
    seconds = math.floor((duration / 1000) % 60)
    minutes = math.floor((duration / (1000 * 60)) % 60)
# discount = True if age >= 65 else False
    if (minutes < 10 ):
        minutesF = "0" + str(minutes)
    else:
        minutesF = str(minutes)
    if (seconds < 10 ):
        secondsF = "0" + str(seconds)
    else:
        secondsF = str(seconds)

    # return minutes + ":" + secondsF + "," + str(milliseconds)
    return str(minutes) + ":" + str(secondsF) + "," + str(milliseconds)
#   return  minutes + ":" + seconds + "." + milliseconds;
# }
