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

    # end alert
    print("Goodbye ISS")

def getnextalert():
    "Return the number of seconds until and duration of the next flyover"
    url = 'http://api.open-notify.org/iss-pass.json'
    querystring = {'lat':lat, 'lon':lon, 'alt':alt, 'n':'1'}
    content = requests.get(url, querystring)
    # Print response headers
    #print(content.headers)
    jsoncontent = content.json()
    # Print content of json download
    #print(jsoncontent)

    # Print server and local times
    print("Server time: " + time.ctime(jsoncontent['request']['datetime']))
    print("Local time:  " + time.ctime())

    risetime = jsoncontent['response'][0]['risetime']
    duration = jsoncontent['response'][0]['duration']
    # Print next rise and duration in human readable form
    print("risetime: " + time.ctime(risetime))
    print("duration: " + str(duration) + " seconds")

    return (int(risetime - time.time()), duration)

def addsked(nextalert, duration):
    "Schedule next alert"
    sked.enter(nextalert, 1, doalert, {duration})
    # Print queue of scheduled tasks
    # print(sked.queue)
    sked.run()

def main():
    while True:
        alerttime, alertduration = getnextalert()
        addsked(alerttime, alertduration)

if __name__ == "__main__":
    main()
