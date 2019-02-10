import json
import requests
import sched
import time

# location variables
lat = "48.4225"
lon = "-123.3585"

# seconds for early warning
earlywarn = 300

# initialize scheduler
sked = sched.scheduler(time.time, time.sleep)

def doalert():
    print("Hello ISS")

def getnextalert():
    "Return the number of seconds until the next flyover"
    content = requests.get("http://api.open-notify.org/iss-pass.json?lat=" + lat + "&lon=" + lon)
    jsoncontent = content.json()
    return int(jsoncontent['response'][0]['risetime'] - earlywarn - time.time())

def addsked(nextalert):
    "Schedule next alert"
    print(nextalert)
    sked.enter(nextalert, 1, doalert)
    sked.run()

def main():
    # Need to loop
    seconds = getnextalert()
    addsked(seconds)

if __name__ == "__main__":
    main()
