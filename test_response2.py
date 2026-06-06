import requests
import pytest


# Base_URL = "https://jsonplaceholder.typicode.com/posts"
# def test_list_API():
#     response = requests.get(Base_URL)
#
#     data = response.json()
#     # print(data)
#     # print(len(data))
#     assert response.status_code == 200
#     assert len(data) == 100
#     assert isinstance(data, list)
#     assert "id" in data[0]
#     assert "userId" in data[0]
#     assert "title" in data[0]
#     assert "body" in data[0]


#####################################################

BASE_URL = "https://jsonplaceholder.typicode.com/posts"

@pytest.fixture()
def api_response():
    response = requests.get(f"{BASE_URL}")
    return response


def test_type_data(api_response):
    data = api_response.json()
    assert isinstance(data, list)

def test_status_code_check(api_response):
    assert api_response.status_code == 200

def test_exist_keys_in_data(api_response):
    data = api_response.json()
    assert "id" in data[0]
    assert "userId" in data[0]
    assert "title" in data[0]
    assert "body" in data[0]

def test_len_of_data(api_response):
    data = api_response.json()
    assert len(data) == 100