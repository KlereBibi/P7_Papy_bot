import requests
import json

import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from entities.coord import Coord

class ApiManager:
    
    def apistreet(self):
        res = requests.get("http://open.mapquestapi.com/nominatim/v1/search.php?key=F3SzABt6KmK3CyhsZPFa96ucMZ3APqGT&format=json&postalcode=93470&state=France")
        read = json.loads(res.text)
        
        for element in read:
            place = Coord(element['lat'], element['lon'])
            
        return place

apimanager = ApiManager()
apimanager.apistreet()