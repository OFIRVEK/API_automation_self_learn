import requests
import pytest


BASE_URL = "https://jsonplaceholder.typicode.com/posts/1"
payload = {"id": 1, "title": "Updated Title", "body": "Updated body", "userId": 1}

@pytest.fixture()
def put_test():
    response = requests.put(BASE_URL, json=payload)
    return response

def test_code_stat(put_test):
    assert put_test.status_code == 200

def test_title_value(put_test):

    assert put_test.json()["title"] == "Updated Title"

def test_id_value(put_test):
    assert put_test.json()["id"] == 1

