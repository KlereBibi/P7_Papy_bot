import requests
import json
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from entities.coord import Coord

class ApiManager:
    
    def apistreet(self, cit, stat):
        res = requests.get("http://open.mapquestapi.com/nominatim/v1/search.php?key=F3SzABt6KmK3CyhsZPFa96ucMZ3APqGT&format=json&city={}&state={}".format(cit, stat))
        read = json.loads(res.text)
        first_choice = read[0]
        place = Coord(first_choice['lat'], first_choice['lon'])
            
        return place

    def search_name(self, lat, lon):
        res = requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&list=geosearch&gscoord={}%7C {}&gsradius=10000&gslimit=100".format(lat,lon))
        read = json.loads(res.text)
        title = (((read['query'])["geosearch"])[0])['title']
        return title

    def search_art(self, title):
        res = requests.get("https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={}".format(title))
        read = json.loads(res.text)
        search = ((read["query"])["pages"]).values()
        for element in search: 
            resume = element['extract']
        print(resume)
        return resume

        
        
