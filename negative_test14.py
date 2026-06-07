import pytest
import requests

base_url = "https://jsonplaceholder.typicode.com/posts"

@pytest.mark.parametrize("invalid_userId", [99999,-1, pytest.param("abc", marks=pytest.mark.xfail(reason="JSONPlaceholder may not reject invalid types"))])
def test_invalid_params(invalid_userId):
    response = requests.get(base_url, params={"userId":invalid_userId})
    assert response.status_code == 200
    assert len(response.json()) == 0
    assert isinstance(response.json(), list)

# def test_non_exist_data(invalid_params):
#     assert invalid_params.status_code == 200
#     assert len(invalid_params.json()) == 0
#     assert isinstance(invalid_params.json(), list)
#
# @pytest.mark.xfail(reason="JSONPlaceholder may not reject these")
# def test_invalid_data(invalid_params):
#     assert invalid_params.status_code == 400


