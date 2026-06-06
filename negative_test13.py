import pytest
import requests

base_url = "https://jsonplaceholder.typicode.com/posts"

@pytest.mark.parametrize("invalid_data_types", [pytest.param({'title': 12345, 'body': 'text', 'userId': 1}, id ="wrong title"),pytest.param({'title': 'text', 'body': 'text', 'userId': 'abc'}, id="wrong userId"),
                                                pytest.param({'title': True, 'body': False, 'userId': 1}, id= "wrong body")])


@pytest.mark.xfail(reason="JSONPlaceholder accepts wrong data types, real API should return 400")
def test_data_types(invalid_data_types):
    response = requests.post(base_url, json=invalid_data_types)
    assert response.status_code ==400
