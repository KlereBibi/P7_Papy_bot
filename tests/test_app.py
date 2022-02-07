
import pytest

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from app import create_app
from flask import render_template
import json

@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client

def test_should_status_code_ok_get(client):
    response = client.get('/')
    assert response.status_code == 200
    data = response.data.decode()
    assert data == render_template('index.html')

 
def test_should_status_code_ok_post(client, mocker):

    return_val = {'username' : 'testUser'}
    mocker.patch('flask.Request.form', return_value = return_val)
    mocker.patch('controller.control.Control.search_article', return_value = {"name": "Claire", "competence" : "perfect"})
    excepted_value = {"name": "Claire", "competence" : "perfect"}
    response = client.post('/ajax', data=excepted_value)

    assert response.status_code == 200

    data = response.data.decode()
    result = json.loads(data)
    assert result == excepted_value
