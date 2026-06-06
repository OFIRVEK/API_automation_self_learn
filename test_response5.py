import requests
import pytest


BASE_URL = "https://jsonplaceholder.typicode.com/posts/1"
@pytest.fixture()
def delete_check():
    response = requests.delete(BASE_URL)
    return response

def test_code_stat(delete_check):
    assert delete_check.status_code == 200

def test_empty_json(delete_check):
    assert delete_check.json() == {}


########This test is meant to check if the {} is really empty: after deletion we send GET request again and assert status_code == 404

# def test_post_is_gone(delete_check):
#     # After delete, try to GET the same resource
#     response = requests.get(BASE_URL)
#
#     # Server should return 404 - resource no longer exists
#     assert response.status_code == 404