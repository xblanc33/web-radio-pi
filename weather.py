import urllib2, urllib, json
baseurl = "https://www.prevision-meteo.ch/services/json/gradignan"
result = urllib2.urlopen(baseurl).read()
data = json.loads(result)
print data["fcst_day_0"]["date"]

