#!/usr/bin/env python

import urllib2
import json

wurl = urllib2.urlopen("http://api.wunderground.com/api/<api-key-here>/conditions/astronomy/forecast/q/TX/KSAT.json")
json_string = wurl.read()
parsed_json = json.loads(json_string)

temp_f = parsed_json['current_observation']['temp_f']
conditions = parsed_json['current_observation']['weather']
relative_humidity = parsed_json['current_observation']['relative_humidity']
visi = parsed_json['current_observation']['visibility_mi']
wind_string = parsed_json['current_observation']['wind_string'].replace("F", "f")
wind = wind_string.replace("Gusting", "\nGusting")
UV = parsed_json['current_observation']['UV']
sunrise_hour = parsed_json['moon_phase']['sunrise']['hour']
sunrise_minute = parsed_json['moon_phase']['sunrise']['minute']
sunset_hour = parsed_json['moon_phase']['sunset']['hour']
sunset_minute = parsed_json['moon_phase']['sunset']['minute']

print temp_f, "F"
print conditions
print "Humidity:", relative_humidity
print "Wind", wind
print "Visibility:", visi, "miles"
print "Sunrise @ " + sunrise_hour + ":" + sunrise_minute
print "Sunset @ " + sunset_hour + ":" + sunset_minute
print "UV Index:", UV, "\n"

for data in parsed_json['forecast']['simpleforecast']['forecastday']:
    print data['date']['weekday'] + ':'
    print data['conditions']
    print "Highs:", data['high']['fahrenheit'], "Lows:", data['low']['fahrenheit'], "\n", data['pop'], "% Chance of rain \n"

wurl.close()
