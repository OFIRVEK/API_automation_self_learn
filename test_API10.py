import pytest
import requests

url = "https://jsonplaceholder.typicode.com/posts"

@pytest.mark.parametrize("invalid_id", [99999, 0, -1, 99999999, pytest.param(1,marks=pytest.mark.xfail(reason = "we expect to get 200"))])##Bonus 1
def test_invalid_ids(invalid_id):
    response = requests.get(f"{url}/{invalid_id}")
    print(response.status_code) #####Bonus2 question
    assert response.status_code == 404




