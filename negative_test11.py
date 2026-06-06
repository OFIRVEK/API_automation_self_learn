import pytest
import requests


base_url = "https://jsonplaceholder.typicode.com/posts"

@pytest.mark.parametrize("invalid_payload", [{}, {'title': 'only title'},{'userId': 1}])
@pytest.mark.xfail(reason="JSONPlaceholder doesn't actually save POSTed data")
def test_broken_payload(invalid_payload):
    response = requests.post(base_url, json=invalid_payload)
    assert response.status_code == 400
    assert len(response.json()) > 0





