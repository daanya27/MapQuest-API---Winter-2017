import urllib.parse
import urllib.request
import json


### API STUFF


BASE_URL = "http://open.mapquestapi.com/directions/v2/route?"
BASE_ELEV_URL = "http://open.mapquestapi.com/elevation/v1/profile?"

KEY = "10uEWhCB5WKuQ2IGAcocTuyEikkUK8Yk"


def build_url(user_input: list) -> str:
    ''' Builds URL depending on what user types in '''

    url_components = [("key", KEY)]
    locations = user_input[1]
    
    for location in locations:
        if len(url_components) == 1:
            url_components.append(("from", location))
        else:
            url_components.append(("to", location))

    full_url = BASE_URL + urllib.parse.urlencode(url_components, encoding="UTF-8")
    return full_url
  

def build_elev_url(user_input: list, json_dict: dict) -> list:
    ''' Builds elevation URLs depending on locations in user_input '''

    urls = []
    
    locations = json_dict["route"]["locations"]
    for place in locations:
        url_components = [("key", KEY), ("shapeFormat", "raw")]
        coordinate_string = ""
        latlong = place["latLng"]
        coordinate_string += str(latlong["lat"]) + ","
        coordinate_string += str(latlong["lng"]) + ","

        url_components.append(("unit", "f"))
        
        url_components.append(("latLngCollection", coordinate_string[:-1]))

        full_url = BASE_ELEV_URL + urllib.parse.urlencode(url_components, encoding="UTF-8")
        urls.append(full_url)

    elevations = []
    for url in urls:
        elev_dict = read_url(url)
        elevations.append(elev_dict["elevationProfile"][0]["height"])

    return elevations
    
        

def read_url(url: str) -> dict:
    ''' Reads url and gives back dict of opened url in JSON '''

    http_response = urllib.request.urlopen(url)
    encoded_bytes = http_response.read()
    json_string = encoded_bytes.decode(encoding='UTF-8')
    json_text = json.loads(json_string)
    
    http_response.close()   #why do we have to close it? what are we opening?
    
    return json_text




