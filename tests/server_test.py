def test_main(client):
    response = client.get('/'
    )
    assert response.status_code == 200


def test_wrong_endpoint(client):
    response = client.get('/school/assignments'
                         )
    assert response.status_code == 404
