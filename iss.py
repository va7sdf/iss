import csv
import json
import os
import requests
import time
from threading import Timer

lat = "48.4225"
lon = "-123.3585"
tempfile = "predictions.csv"

def alertme( jsoncontent ):
    csvfile = open(tempfile, 'a')
    csvwriter = csv.writer(csvfile)

    if os.stat(tempfile).st_size == 0:
        csvwriter.writerow(['RISETIMESTAMP', 'RISETIMEHUMAN', 'ALERTTIMESTAMP', 'ALERTTIMEHUMAN', 'DURATIONSECONDS'])

    csvwriter.writerow([jsoncontent['response'][0]['risetime'],
                       time.ctime(jsoncontent['response'][0]['risetime']),
                       jsoncontent['response'][0]['risetime'] - 300,
                       time.ctime(jsoncontent['response'][0]['risetime'] - 300)])

    csvfile.close()

def main():
    #http://api.open-notify.org/iss-pass.json?lat=LAT&lon=LON
    content = requests.get("http://api.open-notify.org/iss-pass.json?lat=" + lat + "&lon=" + lon)

    jsoncontent = content.json()

    alertme( jsoncontent )

if __name__ == "__main__":
    main()
