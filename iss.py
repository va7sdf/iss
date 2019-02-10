import json
import requests
import sched
import time

# location variables
lat = "48.4225"
lon = "-123.3585"
alt = "8"

# initialize scheduler
sked = sched.scheduler(time.time, time.sleep)

def doalert(duration):

    # start alert
    print("Hello ISS")

    time.sleep(duration)

    print("Goodbye ISS")

def getnextalert():
    "Return the number of seconds until the next flyover"
    content = requests.get("http://api.open-notify.org/iss-pass.json?lat=" + lat + "&lon=" + lon + "&alt=" + alt + "&n=1")
    jsoncontent = content.json()
    return (int(jsoncontent['response'][0]['risetime'] - time.time()),
            int(jsoncontent['response'][0]['duration']))

def addsked(nextalert, duration):
    "Schedule next alert"
    sked.enter(nextalert, 1, doalert, {duration})
    sked.run()

def main():
    # Need to loop
    alerttime, alertduration = getnextalert()
    print(alerttime)
    print(alertduration)
    addsked(alerttime, alertduration)

if __name__ == "__main__":
    main()
