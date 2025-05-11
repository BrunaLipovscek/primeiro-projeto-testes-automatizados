import requests

def test_api_login():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    assert "Leanne Graham" in response.json()["name"]