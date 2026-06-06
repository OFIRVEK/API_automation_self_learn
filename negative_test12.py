import pytest
import requests

base_url = "https://jsonplaceholder.typicode.com/posts/1"
@pytest.mark.parametrize("method", [requests.post,requests.delete, requests.put])
@pytest.mark.xfail(reason="JSONPlaceholder doesn't return 405")

def test_wrong_methods(method):
    response = method(base_url)
    print(response)
    assert response.status_code == 405 or response.status_code == 404
