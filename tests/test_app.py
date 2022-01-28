
import pytest

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from app import create_app

@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client

def test_should_status_code_ok(client):
	response = client.get('/')
	assert response.status_code == 200