"""the module allows you to coordinate and call the different modules of the application"""

from models.manager.apimanager import ApiManager
from models.entities.inputparser import InputParser

class Control:

    """class to coordinate the application"""

    def __init__(self):

        """methode to initialize many class"""

        self.apimanager = ApiManager()
        self.inputparser = InputParser()

    def user_question(self, text_user=None):

        """methode to pars the user question
        return (str): the essential question"""

        pars = self.inputparser.parser(text_user)
        return pars

    def search_geolo(self, text_user):

        """methode to search the coordonate
        return object with latitude and longitude"""

        geolo = self.apimanager.apistreet(self.user_question(text_user))
        return geolo

    def papysorry(self):

        """methode with a papybot text
        return dict with answer of papybot who no found the place"""

        answer = {'papysorry' : "Je suis désolée poussin, mes cellules grises n'ont rien trouvé à ce sujet.",
                'papyprecision' : "Peut-être pourrais-tu reformuler ta demande pour aider ma vieille mémoire?"}
        return answer

    def search_article(self,text_user=None):

        """methode to search article of wikipedia
        return json with information"""

        geolo = self.search_geolo(text_user)
        if geolo:
            article = self.apimanager.apiwiki(geolo.latitude, geolo.longitude)
            if article:
                article['latitude'] = (geolo.latitude)
                article['longitude'] = (geolo.longitude)
                article['result'] = ('finded')
                article['papybot_adress'] = ("Voici ce que j'ai pu te dénicher")
                article['adress'] = (geolo.adress)
                return article
            else:
                return self.papysorry()
        else:
            return self.papysorry()
