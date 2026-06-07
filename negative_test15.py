import pytest
import requests

base_url = "https://jsonplaceholder.typicode.com/posts"

@pytest.mark.parametrize("userId", [99999, -1, 0, 99999999])
@pytest.mark.xfail(reason="JSONPlaceholder returns 200 even for non-existent ids")
def test_invalid_userId(userId):
    response = requests.delete(f"{base_url}/{userId}")
    data = response.json()
    assert response.status_code == 404
    assert len(data) == {}


####bonus:
@pytest.mark.xfail(reason="JSONPlaceholder doesn't truly delete")
def test_idempotency():
    url = f"{base_url}/1"

    response1 = requests.delete(url)
    assert response1.status_code == 200

    response2 = requests.delete(url)
    assert response2.status_code == 404