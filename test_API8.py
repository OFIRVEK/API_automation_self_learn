import pytest
import requests



base_url = "https://jsonplaceholder.typicode.com/posts/1"


#######Part 1
# payload = {'title': 'Patched Title'}
# @pytest.fixture()
# def patch_test():
#     response = requests.patch(base_url, json=payload)
#
#     return response
#
# def test_data_received(patch_test):
#     data = patch_test.json()
#     assert data["title"] == 'Patched Title'
#     assert "userId" in data
#     assert "body" in data
#     assert "id" in data
#     print(data["body"])
#
#
# def test_code_stat(patch_test):
#     assert patch_test.status_code == 200


##########Part 2
payload = {"body": "New body content"}
@pytest.fixture()
def patch_test():
    response1 = requests.get(base_url)
    response2 = requests.patch(base_url, json=payload)

    return response1,response2

def test_data_received(patch_test):
    response1, response2 = patch_test
    original = response1.json()  # GET response — original data
    patched = response2.json()   #Patched data
    assert patched["body"] == payload["body"]
    assert patched["title"] == original["title"]

