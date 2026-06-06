import http
import pytest
import requests

# def test_response():
#     BASE_URL = "https://jsonplaceholder.typicode.com/posts/1"
#     response = requests.get(BASE_URL)
#
#
#     data = response.json()
#     print(data)
#
#
#     assert response.status_code == 200
#     assert data["id"] == 1
#     assert "userId" in data
#     assert "title" in data
#     assert "body" in data
#
#
#
import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def post_response():
    response = requests.get(f"{BASE_URL}/posts/1")
    return response

def test_status_code(post_response):
    assert post_response.status_code == 200

def test_post_id(post_response):
    data = post_response.json()
    assert data["id"] == 1

def test_post_keys(post_response):
    data = post_response.json()
    assert "userId" in data
    assert "title" in data
    assert "body" in data