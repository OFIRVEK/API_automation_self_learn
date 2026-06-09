import pytest
import requests



base_url = "https://reqres.in/api/users"
unique_id = []
@pytest.fixture()
def check_pages(page_number):
    response = requests.get(base_url, params={"page":page_number})


    return response

@pytest.mark.parametrize("page_number", [1,2,3])
def test_append_id(check_pages,page_number):
    data = check_pages.json()["data"]
    for user in data:
        unique_id.append(user["id"])

    assert len(unique_id) == len(set(unique_id))

    assert check_pages.status_code == 200
    assert check_pages.elapsed.total_seconds() < 2  ##for this matter we check API time response that is less than 2 sec
    assert check_pages.json()["page"] == page_number