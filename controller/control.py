import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.manager.apimanager import ApiManager
from models.entities.inputparser import InputParser


class Control: 
    

    def ask_api(self):

        apimanager = ApiManager()
        inputparser = InputParser()
        user_question = "tour eiffel"
        pars = inputparser.parser(user_question)
        geolo = apimanager.apistreet(pars)
        print(geolo.latitude, geolo.longitude)
        title_art = apimanager.search_name(geolo.latitude, geolo.longitude)
        content_art = apimanager.search_art(title_art)
        print(content_art)
        
