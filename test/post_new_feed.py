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

# post non-revealed feed
r = requests.post("http://127.0.0.1:1111/feed",
    data={'user_id': 1, 'content': "this is deneme feed", 'lon': lon,
          'lat': lat, 'target_user_id':2, 'revealed':False, 'token':'12423321542'})
print(r.status_code, r.reason)
print r.text
