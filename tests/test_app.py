
import pytest

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from app import create_app
from flask import render_template

@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client

def test_should_status_code_ok_get(client):
    response = client.get('/')
    assert response.status_code == 200

def test_should_status_code_ok_get_data(mocker, client):
    response = client.get('/')
    data = response.data.decode()
    assert data == render_template('index.html')


def test_should_status_code_ok_post(client):
    username = 'testUser'
    password = 'testPassword'
    response = client.post('/login', data={'username' : username, 'password' : password})
