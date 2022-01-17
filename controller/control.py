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

    def user_question(self, text_user):

        """methode to pars the user question 
        return (str): the essential question"""

        pars = self.inputparser.parser(text_user)
        return pars
    
    def search_geolo(self, text_user):

        """methode to search the coordonate
        return object with latitude and longitude"""
        
        geolo = self.apimanager.apistreet(self.user_question(text_user))
        return geolo

    def search_article(self,text_user):

        """methode to search article of wikipedia
        return json with all information"""
        geolo = self.search_geolo(text_user)
        if geolo:
            article = self.apimanager.apiwiki(geolo.latitude, geolo.longitude)
            article['coord'] = (geolo.latitude, geolo.longitude)
            print(article)
            return article
        else: 
            print("Je suis désolé, je n'ai rien trouvé mon grand.")
        
