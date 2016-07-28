__author__ = 'cpuskarz'
###################
# Example usage
###################
#$ ./geocode.py
#Enter your address:  2850 Premiere Parkway, Duluth, GA
#2850 Premiere Parkway, Duluth, GA 30097, USA is at
#lat: 34.002958
#lng: -84.092877

###################
# First attempt at parsing Google's rest api
###################
#!/usr/bin/python

import requests          # module to make html calls
import json          # module to parse JSON data

#addr_str = raw_input("Enter your address:  ")
addr_str = "2305 N. Verde Dr., Arlington Heights, IL, 60004"

maps_url = "https://maps.googleapis.com/maps/api/geocode/json"
is_sensor = "false"      # do you have a GPS sensor?

payload = {'address': addr_str, 'sensor': is_sensor}

r = requests.get(maps_url,params=payload)

# store the json object output
maps_output = r.json()
print ""
#print "MAP JSON"
#print maps_output
print ""

# create a string in a human readable format of the JSON output for debugging
maps_output_str = json.dumps(maps_output, sort_keys=True, indent=2)
print(maps_output_str)

# once you know the format of the JSON dump, you can create some custom
# list + dictionary parsing logic to get at the data you need to process

# store the top level dictionary
results_list = maps_output['results']
result_status = maps_output['status']


formatted_address = results_list[0]['formatted_address']
result_geo_lat = results_list[0]['geometry']['location']['lat']
result_geo_lng = results_list[0]['geometry']['location']['lng']

print("%s is at\nlat: %f\nlng: %f" % (formatted_address, result_geo_lat, result_geo_lng))