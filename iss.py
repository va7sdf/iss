import json
import requests
import sched
import time

lat = "48.4225"
lon = "-123.3585"

def alertme(jsoncontent):
    return time.ctime(jsoncontent['response'][0]['risetime'] - 300)

def main():
    #http://api.open-notify.org/iss-pass.json?lat=LAT&lon=LON
    content = requests.get("http://api.open-notify.org/iss-pass.json?lat=" + lat + "&lon=" + lon)

    jsoncontent = content.json()

    print(alertme(jsoncontent))

if __name__ == "__main__":
    main()
