import urllib.request
import json
import sys
print(sys.path)

class ApiManager:
    
    def apistreet(self):
        res = urllib.request.urlopen("http://open.mapquestapi.com/nominatim/v1/search.php?key=F3SzABt6KmK3CyhsZPFa96ucMZ3APqGT&format=json&postalcode=93470&state=France").read()
        page = res.decode("utf8")
        a = json.loads(page)
        

apimanager = ApiManager()
apimanager.apistreet()