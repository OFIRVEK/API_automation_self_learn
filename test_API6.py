import pytest
import requests


@pytest.mark.parametrize("post_id", [
    1, 2, 3, 5, 10,
    pytest.param(999, marks=pytest.mark.xfail(reason="post does not exist"))
])
def test_multiple_post(post_id):
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    response = requests.get(url)
    data = response.json()


    assert response.status_code == 200
    assert "title" in data
    assert data["id"] == post_id

