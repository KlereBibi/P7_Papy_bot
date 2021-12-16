import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.entities.apimanager import ApiManager

class Control: 

    def ask_api(self):

        apimanager = ApiManager()
        geolo = apimanager.apistreet("Coubron", "France")
        title_art = apimanager.search_name(geolo.latitude, geolo.longitude)
        content_art = apimanager.search_art(title_art)
        
