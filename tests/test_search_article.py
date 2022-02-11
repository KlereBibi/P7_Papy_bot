""" this module is the test of methode search article in control.py """

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from controller.control import Control
from models.entities.coord import Coord

def test_search_article_geolo_false(mocker):
    mocker.patch('controller.control.Control.user_question', return_value = False)
    mocker.patch('controller.control.Control.search_geolo', return_value = False)
    sut = Control()
    expected_value = {'papysorry' : "Je suis désolée poussin, mes cellules grises n'ont rien trouver à ce sujet.",
                'papyprecision' : "Peut-être pourrais-tu reformuler ta demande pour aider ma vieille mémoire?"}
    rep = sut.search_article(None)
    assert rep == expected_value

def test_search_article_geolo_valid_wiki_false(mocker):
    mocker.patch('controller.control.Control.user_question', return_value = True)
    simul_coord = Coord('41.5986442', '-90.3434618', 'Le Claire, Scott County, Iowa, United States of America')
    mocker.patch('controller.control.Control.search_geolo', return_value = simul_coord)
    mocker.patch('models.manager.apimanager.ApiManager.apiwiki', return_value = False)
    sut = Control()
    expected_value = {'papysorry' : "Je suis désolée poussin, mes cellules grises n'ont rien trouver à ce sujet.",
                'papyprecision' : "Peut-être pourrais-tu reformuler ta demande pour aider ma vieille mémoire?"}
    rep = sut.search_article(None)
    assert rep == expected_value

def test_search_article_geolo_valid_wiki_true(mocker):
    mocker.patch('controller.control.Control.user_question', return_value = True)
    simul_coord = Coord('41.5986442', '-90.3434618', 'Le Claire, Scott County, Iowa, United States of America')
    mocker.patch('controller.control.Control.search_geolo', return_value = simul_coord)
    mocker.patch('models.manager.apimanager.ApiManager.apiwiki', return_value = {'title': 'Le Claire', 
                                                                                'papybot': 'Mes petites cellules grises se souviennent de bien des choses. ',
                                                                                'extract': 'Le Claire est une ville située dans le comté de Scott, dans l’État de l’Iowa, aux États-Unis. Lors du recensement de 2010, sa population s’élevait à 3 765 habitants.', 
                                                                                'fullurl': 'https://fr.wikipedia.org/wiki/Le_Claire', 
                                                                                'latitude': '41.5986442', 'longitude': '-90.3434618', 
                                                                                'result': 'finded', 'papybot_adress': "Voici ce que j'ai pu te dénicher", 
                                                                                'adress': 'Le Claire, Scott County, Iowa, United States of America'})
    sut = Control()
    request_value = {'title': 'Le Claire', 
                    'papybot': 'Mes petites cellules grises se souviennent de bien des choses. ',
                    'extract': 'Le Claire est une ville située dans le comté de Scott, dans l’État de l’Iowa, aux États-Unis. Lors du recensement de 2010, sa population s’élevait à 3 765 habitants.', 
                    'fullurl': 'https://fr.wikipedia.org/wiki/Le_Claire', 
                    'latitude': '41.5986442', 'longitude': '-90.3434618', 
                    'result': 'finded', 'papybot_adress': "Voici ce que j'ai pu te dénicher", 
                    'adress': 'Le Claire, Scott County, Iowa, United States of America'}
    rep = sut.search_article(None)
    assert rep == request_value
    