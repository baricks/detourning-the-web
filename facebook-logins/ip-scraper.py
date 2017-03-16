import json
from pprint import pprint
import geocoder
from PIL import Image, ImageDraw, ImageFont
from subprocess import call, check_call
import sys
import urllib2
import requests
import glob
import time
import re
import os

def captionImage(filename, action, date, location):
        im = Image.open(filename)
        canvas = ImageDraw.Draw(im)
        fnt = ImageFont.truetype('/Users/rebeccaricks/Library/Fonts/Apercu Bold.otf', 30)
        final_text = action + "\n" + date + "\n" + location
        canvas.text((10,200), final_text, font=fnt, fill=(255,255,255))
        im.save(filename)

def downloadImage(coords, action, date, location):
    # print "downloading image"
    for k in range(130,200,5):
        url = "https://maps.googleapis.com/maps/api/streetview?size=800x500&location=" + coords + "&heading=" + str(k) + "&pitch=-1&scale=2&key=" + YOURAPIKEY
        print url

        filename = coords + ("-") + str(k) + '.png'

        r = requests.get(url, stream=True)
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

        # Caption image
        captionImage(filename, action, date, location)

def lookupIP(ip_address, action, date):
    # print "looking up IP address"
    g = geocoder.ip(ip_address)
    lat = g.latlng[0]
    lon = g.latlng[1]
    city = g.city
    state = g.state
    location = city + ", " + state

    coords = str(lat) + "," + str(lon)

    # Download the image from Google Maps
    downloadImage(coords, action, date, location)

# Open json file
with open('data.json') as data_file:
    data = json.load(data_file)
    stuff = data["Administrative Records"]

# Cycle through to grab action, date, and IP address
for i in range(0, len(stuff)):
    action = stuff[i]["Action"]
    date = stuff[i]["Created"]
    ip_address = stuff[i]["IP Address"]

    print action
    print date
    print ip_address

    # Get lat/lon coordinates from IP address lookup
    lookupIP(ip_address, action, date)
