import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.manager.apimanager import ApiManager
import requests

def test_apiwiki_statut_false(mocker):
    return_val = requests.Response()
    mocker.patch('requests.get', return_value = return_val)
    return_val.status_code = 400
    sut = ApiManager()
    assert  sut.apiwiki(None, None) is False

def test_apiwiki_statut_valide_rep_empty(mocker):
    return_val = requests.Response()
    return_val.status_code = 200
    excepted_value = {}
    def json_func(): 
        return excepted_value
    return_val.json = json_func
    mocker.patch('requests.get', return_value = return_val)
    sut = ApiManager()
    assert  sut.apiwiki(None, None) is False

def test_apiwiki_statut_valide_rep_false(mocker):
    return_val = requests.Response()
    return_val.status_code = 200
    excepted_value = {'title' : 'pouet'}
    def json_func(): 
        return excepted_value
    return_val.json = json_func
    mocker.patch('requests.get', return_value = return_val)
    sut = ApiManager()
    assert  sut.apiwiki(None, None) is False

def test_apiwiki_statut_valide_rep_no_answer(mocker):
    return_val = requests.Response()
    return_val.status_code = 200
    excepted_value = {'continue': {'excontinue': 1, 'continue': '||info'}, 'query': {'pages': ''}}
    def json_func(): 
        return excepted_value
    return_val.json = json_func
    mocker.patch('requests.get', return_value = return_val)
    sut = ApiManager()
    assert  sut.apiwiki(None, None) is False
    

def test_apiwiki_statut_valide_rep_valid(mocker):
    return_val = requests.Response()
    return_val.status_code = 200
    def json_func():
        return {'continue': {'excontinue': 1, 'continue': '||info'}, 'query': {'pages': {'7771525': \
        {'pageid': 7771525, 'ns': 0, 'title': 'Le Claire', 'index': -1, \
        'extract': 'Le Claire est une ville située dans le comté de Scott, dans l’État de l’Iowa, aux États-Unis. Lors du recensement de 2010, sa population s’élevait à 3 765 habitants.', \
        'contentmodel': 'wikitext', 'pagelanguage': 'fr', 'pagelanguagehtmlcode': 'fr', \
        'pagelanguagedir': 'ltr', 'touched': '2022-01-25T13:38:57Z', 'lastrevid': 182775912, 'length': 2270, \
        'fullurl': 'https://fr.wikipedia.org/wiki/Le_Claire', 
        'editurl': 'https://fr.wikipedia.org/w/index.php?title=Le_Claire&action=edit', \
        'canonicalurl': 'https://fr.wikipedia.org/wiki/Le_Claire'},\
        '11126463': {'pageid': 11126463, 'ns': 0, 'title': 'Le Claire Township (comté de Scott, Iowa)',\
        'index': 0, 'contentmodel': 'wikitext', 'pagelanguage': 'fr', 'pagelanguagehtmlcode': 'fr', \
        'pagelanguagedir': 'ltr', 'touched': '2022-01-25T13:46:28Z', 'lastrevid': 166412675, 'length': 2076, \
        'fullurl': 'https://fr.wikipedia.org/wiki/Le_Claire_Township_(comt%C3%A9_de_Scott,_Iowa)', \
        'editurl': 'https://fr.wikipedia.org/w/index.php?title=Le_Claire_Township_(comt%C3%A9_de_Scott,_Iowa)&action=edit',\
        'canonicalurl': 'https://fr.wikipedia.org/wiki/Le_Claire_Township_(comt%C3%A9_de_Scott,_Iowa)'}, \
        '11126476': {'pageid': 11126476, 'ns': 0, 'title': 'Pleasant Valley Township (comté de Scott, Iowa)', \
        'index': 1, 'contentmodel': 'wikitext', 'pagelanguage': 'fr', 'pagelanguagehtmlcode': 'fr', \
        'pagelanguagedir': 'ltr', 'touched': '2022-01-25T13:46:28Z', 
        'lastrevid': 149377700, 'length': 2091, \
        'fullurl': 'https://fr.wikipedia.org/wiki/Pleasant_Valley_Township_(comt%C3%A9_de_Scott,_Iowa)',\
        'editurl': 'https://fr.wikipedia.org/w/index.php?title=Pleasant_Valley_Township_(comt%C3%A9_de_Scott,_Iowa)&action=edit'\
        , 'canonicalurl': 'https://fr.wikipedia.org/wiki/Pleasant_Valley_Township_(comt%C3%A9_de_Scott,_Iowa)'}, \
        '11638250': {'pageid': 11638250, 'ns': 0, 'title': 'Coe Township (Illinois)', 'index': 2, 'contentmodel': 'wikitext',\
        'pagelanguage': 'fr', 'pagelanguagehtmlcode': 'fr', 'pagelanguagedir': 'ltr', 'touched': '2022-01-25T13:47:45Z', \
        'lastrevid': 171862231, 'length': 2216, 'fullurl': 'https://fr.wikipedia.org/wiki/Coe_Township_(Illinois)',\
        'editurl': 'https://fr.wikipedia.org/w/index.php?title=Coe_Township_(Illinois)&action=edit', \
        'canonicalurl': 'https://fr.wikipedia.org/wiki/Coe_Township_(Illinois)'}, '11638481': \
        {'pageid': 11638481, 'ns': 0, 'title': 'Hampton Township (Illinois)', 'index': 3, 'contentmodel': 'wikitext',\
        'pagelanguage': 'fr', 'pagelanguagehtmlcode': 'fr', 'pagelanguagedir': 'ltr', 'touched': '2022-01-25T13:47:45Z',\
        'lastrevid': 171862200, 'length': 2226, 'fullurl': 'https://fr.wikipedia.org/wiki/Hampton_Township_(Illinois)', \
        'editurl': 'https://fr.wikipedia.org/w/index.php?title=Hampton_Township_(Illinois)&action=edit', \
        'canonicalurl': 'https://fr.wikipedia.org/wiki/Hampton_Township_(Illinois)'}, '11640754': \
        {'pageid': 11640754, 'ns': 0, 'title': 'Port Byron Township', 'index': 4, 'contentmodel': 'wikitext',\
        'pagelanguage': 'fr', 'pagelanguagehtmlcode': 'fr', 'pagelanguagedir': 'ltr', 'touched': '2022-01-25T13:47:45Z',\
        'lastrevid': 171862148, 'length': 2264, 'fullurl': 'https://fr.wikipedia.org/wiki/Port_Byron_Township', \
        'editurl': 'https://fr.wikipedia.org/w/index.php?title=Port_Byron_Township&action=edit', \
        'canonicalurl': 'https://fr.wikipedia.org/wiki/Port_Byron_Township'}, \
        '12578377': {'pageid': 12578377, 'ns': 0, 'title': 'Hampton (Illinois)', 'index': 5, \
        'contentmodel': 'wikitext', 'pagelanguage': 'fr', 'pagelanguagehtmlcode': 'fr', \
        'pagelanguagedir': 'ltr', 'touched': '2022-01-25T13:50:37Z', 'lastrevid': 171862131, \
        'length': 3341, 'fullurl': 'https://fr.wikipedia.org/wiki/Hampton_(Illinois)', \
        'editurl': 'https://fr.wikipedia.org/w/index.php?title=Hampton_(Illinois)&action=edit', \
        'canonicalurl': 'https://fr.wikipedia.org/wiki/Hampton_(Illinois)'}, '12582496': \
        {'pageid': 12582496, 'ns': 0, 'title': 'Port Byron (Illinois)', 'index': 6, \
        'contentmodel': 'wikitext', 'pagelanguage': 'fr', 'pagelanguagehtmlcode': 'fr', \
        'pagelanguagedir': 'ltr', 'touched': '2022-01-25T13:50:38Z', 'lastrevid': 171862120, \
        'length': 3308, 'fullurl': 'https://fr.wikipedia.org/wiki/Port_Byron_(Illinois)', \
        'editurl': 'https://fr.wikipedia.org/w/index.php?title=Port_Byron_(Illinois)&action=edit', \
        'canonicalurl': 'https://fr.wikipedia.org/wiki/Port_Byron_(Illinois)'}, '12584304': \
        {'pageid': 12584304, 'ns': 0, 'title': 'Rapids City (Illinois)', 'index': 7, \
        'contentmodel': 'wikitext', 'pagelanguage': 'fr', 'pagelanguagehtmlcode': 'fr', \
        'pagelanguagedir': 'ltr', 'touched': '2022-01-25T13:50:39Z', 'lastrevid': 171862117,\
        'length': 3246, 'fullurl': 'https://fr.wikipedia.org/wiki/Rapids_City_(Illinois)', \
        'editurl': 'https://fr.wikipedia.org/w/index.php?title=Rapids_City_(Illinois)&action=edit', 
        'canonicalurl': 'https://fr.wikipedia.org/wiki/Rapids_City_(Illinois)'}, 
        '14506985': {'pageid': 14506985, 'ns': 0, 'title': 'Lone Star (pousseur)', 
        'index': 8, 'contentmodel': 'wikitext', 'pagelanguage': 'fr', 'pagelanguagehtmlcode': 'fr',
        'pagelanguagedir': 'ltr', 'touched': '2022-01-25T13:55:59Z', 'lastrevid': 189167222, 
        'length': 4055, 'fullurl': 'https://fr.wikipedia.org/wiki/Lone_Star_(pousseur)', 
        'editurl': 'https://fr.wikipedia.org/w/index.php?title=Lone_Star_(pousseur)&action=edit', 
        'canonicalurl': 'https://fr.wikipedia.org/wiki/Lone_Star_(pousseur)'}}}}

    return_val.json = json_func
    mocker.patch('requests.get', return_value = return_val)
    sut = ApiManager()
    expected_value = {'title': 'Le Claire', 
    'papybot': 'Mes petites cellules grises se souviennent de bien des choses. ',
     'extract': 'Le Claire est une ville située dans le comté de Scott, dans l’État de l’Iowa, aux États-Unis. Lors du recensement de 2010, sa population s’élevait à 3 765 habitants.', 'fullurl': 'https://fr.wikipedia.org/wiki/Le_Claire'}
    value = sut.apiwiki(None, None)
    assert value == expected_value
