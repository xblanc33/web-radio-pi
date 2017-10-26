#!/usr/bin/python

# Weather forecast for Raspberry Pi w/Adafruit Mini Thermal Printer.
# Retrieves data from Yahoo! weather, prints current conditions and
# forecasts for next two days.  See timetemp.py for a different
# weather example using nice bitmaps.
# Written by Adafruit Industries.  MIT license.
# 
# Required software includes Adafruit_Thermal and PySerial libraries.
# Other libraries used are part of stock Python install.
# 
# Resources:
# http://www.adafruit.com/products/597 Mini Thermal Receipt Printer
# http://www.adafruit.com/products/600 Printer starter pack

from __future__ import print_function
import urllib2, urllib, json, time
from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
deg     = chr(0xf8) # Degree symbol on thermal printer

# Fetch forecast data from Yahoo!, parse resulting XML
baseurl = "https://www.prevision-meteo.ch/services/json/gradignan"
result = urllib2.urlopen(baseurl).read()
data = json.loads(result)

# Print heading
printer.inverseOn()
head = data["city_info"]["name"] + " le " + data["fcst_day_0"]["date"]
printer.println('{:^32}'.format(head)) 
printer.inverseOff()

# Print current conditions
printer.boldOn()
printer.println('{:^32}'.format('Previsions:'))
printer.boldOff()
tmin = "minimum = "+str(data["fcst_day_0"]["tmin"])
tmax = "maximum = "+str(data["fcst_day_0"]["tmax"])
cond = data["fcst_day_0"]["condition"].encode('ascii','ignore')
printer.println(tmin)
printer.println(tmax)
printer.println(cond)
printer.boldOn()


printer.feed(3)
