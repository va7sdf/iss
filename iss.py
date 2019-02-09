import json
import requests
import sched
import time

lat = "48.4225"
lon = "-123.3585"
sked = sched.scheduler(time.time, time.sleep)

def foo():
    print("Hello ISS")

def getnextalert(jsoncontent):
    return int(jsoncontent['response'][0]['risetime'] - 800 - time.time())

def addsked(nextalert):
    print(nextalert)
    sked.enter(nextalert, 1, foo)
    sked.run()
    # Call function to perform alert operation

def main():
    # Need to loop

    #http://api.open-notify.org/iss-pass.json?lat=LAT&lon=LON
    content = requests.get("http://api.open-notify.org/iss-pass.json?lat=" + lat + "&lon=" + lon)
    jsoncontent = content.json()
    print(jsoncontent)
    addsked(getnextalert(jsoncontent))

if __name__ == "__main__":
    main()
