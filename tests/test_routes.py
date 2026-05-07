from models.user import User

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_get_all_users_empty(client):
    response = client.get("/user/")
    assert response.status_code == 200
    assert response.json() == []

def test_create_user(client):
    user_data = {
        "BenutzerName": "newuser",
        "BenutzerPWD": "secretpassword"
    }
    response = client.post("/user/create-user", json=user_data)
    assert response.status_code == 200
    data = response.json()
    assert data["BenutzerName"] == "newuser"
    assert data["BenutzerID"] == 1

def test_get_all_users_with_data(client, db_session):
    # Add a user directly to the test DB
    db_session.add(User(BenutzerID=1, BenutzerName="test1", BenutzerPWD="pw1"))
    db_session.commit()
    
    response = client.get("/user/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["BenutzerName"] == "test1"
