import requests
import pytest


BASE_URL = "https://jsonplaceholder.typicode.com/posts"
payload = {"title": 'My Test Post', "body": 'Hello world', "userId": 1 }
@pytest.fixture()
def post_check():
    response = requests.post(BASE_URL, json=payload)
    return response

def test_code_stat(post_check):
    assert post_check.status_code == 201

def test_key_exist(post_check):
    assert "id" in post_check.json()

def test_compare_values(post_check):
    assert payload["title"] == post_check.json()["title"]

