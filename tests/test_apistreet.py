""" this module is the test of methode apistreet of class apimanager """

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from models.manager.apimanager import ApiManager
import requests
from models.entities.coord import Coord

def test_apistreet_statut_false(mocker):
    return_val = requests.Response()
    mocker.patch('requests.get', return_value = return_val)
    return_val.status_code = 400
    sut = ApiManager()
    assert  sut.apistreet(None) is False

def test_apistreet_statut_valide_rep_false(mocker):
    return_val = requests.Response()
    return_val.status_code = 200
    def json_func(): {}
    return_val.json = json_func
    mocker.patch('requests.get', return_value = return_val)
    sut = ApiManager()
    assert  sut.apistreet(None) is False

def test_apistreet_statut_valide_rep_valid(mocker):
    return_val = requests.Response()
    return_val.status_code = 200
    def json_func():
        return {'place_id': '187159358', 'licence': 'Data © OpenStreetMap contributors, \
                ODbL 1.0. https://www.openstreetmap.org/copyright', 'osm_type': 'relation',\
                'osm_id': '129010', 'boundingbox': ['41.580633', '41.613911', '-90.405849',\
                '-90.339528'], 'lat': '41.5986442', 'lon': '-90.3434618',\
                'display_name': 'Le Claire, Scott County, Iowa, United States of America',
                'class': 'boundary', 'type': 'administrative', 
                'importance': 0.20167999693412,
                'icon': 'http://ip-10-98-162-50.mq-us-east-1.ec2.aolcloud.net/nominatim/images/mapicons/poi_boundary_administrative.p.20.png'},\
                {'place_id': '187528167', 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright',\
                'osm_type': 'relation', 'osm_id': '2736400', \
                'boundingbox': ['49.36402', '49.4192126', '0.2134797', '0.2328111'], \
                'lat': '49.3952271', 'lon': '0.218505', 
                'display_name': 'La Claire, Lisieux, Calvados, Normandie, France métropolitaine, 14603, France',\
                'class': 'waterway', 'type': 'river', 'importance': 0.1875},\
                {'place_id': '80991804', 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright',\
                'osm_type': 'way', 'osm_id': '34720584', 'boundingbox': ['49.7495168', '49.7517768', '4.8851524', '4.8887235'], \
                'lat': '49.750767', 'lon': '4.8867991', 'display_name': 'La Claire, Vrigne-aux-Bois, Sedan, Ardennes, Grand Est, France métropolitaine, 08330, France',\
                'class': 'waterway', 'type': 'stream', 'importance': 0.18125}, {'place_id': '24092622', 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright',\
                'osm_type': 'node', 'osm_id': '2366223429', 'boundingbox': ['49.5109922', '49.5509922', '-1.5737539', '-1.5337539'], \
                'lat': '49.5309922', 'lon': '-1.5537539', 'display_name': 'Claire, Cherbourg, Manche, Normandie, France métropolitaine, France',\
                'class': 'place', 'type': 'hamlet', 'importance': 0.16875, 'icon': 'http://ip-10-98-162-50.mq-us-east-1.ec2.aolcloud.net/nominatim/images/mapicons/poi_place_village.p.20.png'},\
                {'place_id': '21482307', 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright',\
                'osm_type': 'node', 'osm_id': '2136224292', 'boundingbox': ['46.5268025', '46.5668025', '1.8308408', '1.8708408'], \
                'lat': '46.5468025', 'lon': '1.8508408', 'display_name': 'La Claire, La Châtre, Indre, Centre-Val de Loire, France métropolitaine, France', \
                'class': 'place', 'type': 'hamlet', 'importance': 0.16875, 'icon': 'http://ip-10-98-162-50.mq-us-east-1.ec2.aolcloud.net/nominatim/images/mapicons/poi_place_village.p.20.png'}, \
                {'place_id': '54498207', 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright', \
                'osm_type': 'node', 'osm_id': '4321344878', 'boundingbox': ['13.8070167', '13.8470167', '15.7231167', '15.7631167'], \
                'lat': '13.8270167', 'lon': '15.7431167', 'class': 'place', 'type': 'hamlet', \
                'importance': 0.16875, 'icon': 'http://ip-10-98-162-50.mq-us-east-1.ec2.aolcloud.net/nominatim/images/mapicons/poi_place_village.p.20.png'}, \
                {'place_id': '51151872', 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright', \
                'osm_type': 'node', 'osm_id': '4026457546', 'boundingbox': ['49.1895878', '49.2095878', '5.2637676', '5.2837676'], \
                'lat': '49.1995878', 'lon': '5.2737676', 'display_name': 'La Claire, Chattancourt, Verdun, Meuse, Grand Est, France métropolitaine, 55100, France', \
                'class': 'place', 'type': 'locality', 'importance': 0.1625, 'icon': 'http://ip-10-98-162-50.mq-us-east-1.ec2.aolcloud.net/nominatim/images/mapicons/poi_place_village.p.20.png'}, \
                {'place_id': '48022686', 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright', 'osm_type': 'node', 'osm_id': '3638383839', \
                'boundingbox': ['45.9791073', '45.9792073', '-1.0739896', '-1.0738896'], 'lat': '45.9791573', 'lon': '-1.0739396', 'display_name': 'La Claire, Fouras, Rochefort, Charente-Maritime, Nouvelle-Aquitaine, France métropolitaine, 17450, France',\
                'class': 'place', 'type': 'isolated_dwelling', 'importance': 0.1625}, {'place_id': '7989110', 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright', \
                'osm_type': 'node', 'osm_id': '864486349', 'boundingbox': ['47.9584733', '47.9784733', '-1.7326404', '-1.7126404'], 'lat': '47.9684733', 'lon': '-1.7226404', 'display_name': 'La Claire, Laillé, Rennes, Ille-et-Vilaine, Bretagne, France métropolitaine, 35890, France',\
                'class': 'place', 'type': 'locality', 'importance': 0.1625, 'icon': 'http://ip-10-98-162-50.mq-us-east-1.ec2.aolcloud.net/nominatim/images/mapicons/poi_place_village.p.20.png'}, {'place_id': '58488345',\
                'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://www.openstreetmap.org/copyright', 'osm_type': 'node', 'osm_id': '4699978288', 'boundingbox': ['43.709693', '43.709793', '-0.1274465', '-0.1273465'],\
                'lat': '43.709743', 'lon': '-0.1273965', 'display_name': 'Claire, Lelin-Lapujolle, Mirande, Gers, Occitanie, France métropolitaine, 32400, France', 'class': 'place', 'type': 'isolated_dwelling', 'importance': 0.1625}
    
    return_val.json = json_func
    mocker.patch('requests.get', return_value = return_val)
    sut = ApiManager()
    geolo = Coord('41.5986442', '-90.3434618', 'Le Claire, Scott County, Iowa, United States of America')
    f_value = sut.apistreet(None)
    assert  f_value.latitude == geolo.latitude
    

    
