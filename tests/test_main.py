def test_index(app, client):
    response = client.get("/")
    assert response.status_code == 200