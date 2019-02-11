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
    "Perform alert"

    # start alert
    print("Hello ISS")

    time.sleep(duration)

    # end alert
    print("Goodbye ISS")

def alerts():
    "Parse JSON file and schedule next five alerts"

    url = 'http://api.open-notify.org/iss-pass.json'
    querystring = {'lat':lat, 'lon':lon, 'alt':alt}
    content = requests.get(url, querystring)
    # Print response headers
    print(content.headers)
    jsoncontent = content.json()
    # Print content of json download
    print(jsoncontent)

    for x in range(0, 5):
        risetime = jsoncontent['response'][x]['risetime']
        duration = jsoncontent['response'][x]['duration']
        # Print next rise and duration in human readable form
        print("risetime: " + time.ctime(risetime))
        print("duration: " + str(duration) + " seconds")

        sked.enter(int(risetime - time.time()), 1, doalert, {duration})

    # Print queue of scheduled tasks
    print(sked.queue)

    sked.run()

def main():
    while True:
        alerts()

if __name__ == "__main__":
    main()
