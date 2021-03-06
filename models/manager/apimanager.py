"""module to search the user question """

import requests
from models.entities.coord import Coord

class ApiManager:
    
    """class to manage all API"""

    def apistreet(self, pars=None):

        """method to search with API openmapqest latitude and longitude
        args :
        city(str) : name of city
        states(str) : name of states
        return (Coord): latitude and longitude"""

        res = requests.get("http://open.mapquestapi.com/nominatim/v1/search.php?q={}&key=F3SzABt6KmK3CyhsZPFa96ucMZ3APqGT&format=json".format(pars))
        if res.status_code == 200:
            read = res.json()
            if read:
                first_choice = read[0]
                place = Coord(first_choice['lat'],
                                first_choice['lon'],
                                first_choice['display_name'])
                return place
            else:
                return False
        else:
            return False

    def apiwiki(self, lat=None, lon=None):


        """Method to search information with Api of Wikipedia
        Args:
        lat (int) : latitude
        lon (int) : longitude
        return (dict) """

        url = "http://fr.wikipedia.org/w/api.php?"

        parameters = {
                        "action": "query",
                        "prop": "extracts|info",
                        "inprop": "url",
                        "explaintext": True,
                        "exsentences": 2,
                        "exlimit": 1,
                        "generator": "geosearch",
                        "ggsradius": 10000,
                        "ggscoord": f"{lat}|{lon}",
                        "format": "json"
        }

        res = requests.get(url, params=parameters)

        if res.status_code == 200:
            content = res.json()

            try:
                content.get("query").get("pages")
            except AttributeError:
                return False
            places = content.get("query").get("pages")
            places_list= []
            for place in places:
                places_list.append(
                                (
                                    places.get(place).get("index"),
                                    places.get(place).get("pageid"),
                                )
                            )
            if not places_list:
                return False
            place_selected = min(places_list)
            pageid_selected = str(place_selected[1])

            article =  {
                    "title": content.get("query")
                    .get("pages")
                    .get(pageid_selected)
                    .get("title", ""),
                    "papybot": 'Mes petites cellules grises se souviennent de bien des choses. ',
                    "extract": content.get("query")
                    .get("pages")
                    .get(pageid_selected)
                    .get("extract", ""),
                    "fullurl": content.get("query")
                    .get("pages")
                    .get(pageid_selected)
                    .get("fullurl", ""),
                }
            return article
        else:
            return False
