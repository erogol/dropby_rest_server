import urllib2
import json
import requests

# Automatically geolocate the connecting IP
f = urllib2.urlopen('http://freegeoip.net/json/')
json_string = f.read()
f.close()
location = json.loads(json_string)
print(location)
location_city = location['city']
location_state = location['region_name']
location_country = location['country_name']

# get location values
content = "Deneme feed!"
lon = location['longitude']
lat = location['latitude']

print "get revealed 3 feeds sent to target user"
r = requests.get("http://127.0.0.1:1111/feed",
    data={'target_user_id': 2, 'content': "this is deneme feed", 'lon': lon,
          'lat': lat, 'revealed':True, 'token':'12423321542', 'N':3})
print(r.status_code, r.reason)
print r.text

print "get non-revealed 3 feeds sent to target user"
r = requests.get("http://127.0.0.1:1111/feed",
    data={'target_user_id': 2, 'content': "this is deneme feed", 'lon': lon,
          'lat': lat, 'revealed':False, 'token':'12423321542', 'N':3})
print(r.status_code, r.reason)
print r.text

print "get non-revealed feed sent to target user"
r = requests.get("http://127.0.0.1:1111/feed",
    data={'target_user_id': 2, 'content': "this is deneme feed", 'lon': lon,
          'lat': lat, 'revealed':False, 'token':'12423321542', 'N':1})
print(r.status_code, r.reason)
print r.text
