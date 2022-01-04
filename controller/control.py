import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.manager.apimanager import ApiManager
from models.entities.inputparser import InputParser


class Control: 
    
    """class to coordinate the application"""

    def __init__(self):

        """methode ti initialize many class"""

        self.apimanager = ApiManager()
        self.inputparser = InputParser()

    def user_question(self):

        """methode to pars the user question 
        return (str): the essential question"""

        user_question = "tour eiffel"
        pars = self.inputparser.parser(user_question)
        return pars
    
    def search_geolo(self):

        """methode to search the coordonate
        return object with latitude and longitude"""
        
        geolo = self.apimanager.apistreet(self.user_question())
        return geolo

    def search_article(self):

        """methode to search article of wikipedia
        return json with all information"""
        geolo = self.search_geolo()
        if geolo:
            article = self.apimanager.apiwiki(geolo.latitude, geolo.longitude)
            print(article)
            return article
        else: 
            print("Je suis désolé, je n'ai rien trouvé mon grand.")
        
