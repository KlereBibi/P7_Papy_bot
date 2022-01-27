import sys
import os
from this import s
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from controller.control import Control

def test_search_article_rep_false(mocker):
    mocker.patch('controller.control.Control.user_question', return_value = False)
    sut = Control()
    no_article = {'papysorry' : "je suis désolée poussin, mes cellules grises n'ont pas rien trouver à ce sujet."}
    rep = sut.search_article(None)
    assert rep == no_article 


