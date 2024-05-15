def test_tasks(test_app):
    """
    Возможно это не то что нужно ...
    """
    response = test_app.get('/tasks')
    body = response.json()
    assert isinstance(body, list) is True
    assert response.status_code == 200


available_body = {
    "id": 0,
    "title": "string",
    "completed": True,
    "created_at": "2024-05-15T08:57:28.392Z",
    "updated_at": "2024-05-15T08:57:28.392Z"
}

title_is_not_exist = {
    "id": 2,
    "title": None,
    "completed": True,
    "created_at": "2024-05-15T08:57:28.392Z",
    "updated_at": "2024-05-15T08:57:28.392Z"
}

string_completed_type = {
    "id": 2,
    "title": "String type",
    "completed": 'true',
    "created_at": "2024-05-15T08:57:28.392Z",
    "updated_at": "2024-05-15T08:57:28.392Z"
}


def test_create_positive_task(test_app):  # +
    response = test_app.post('/tasks', json=available_body)
    assert response.status_code == 422
    assert response.json() == {"detail": "Completed type error"}


def test_create_not_title_task(test_app):  # +
    response = test_app.post('/tasks', json=title_is_not_exist)
    assert response.status_code == 422
    assert response.json() == {"detail": "The title cannot be empty"}


def test_create_string_completed_task(test_app):  # -
    response = test_app.post('/tasks', json=string_completed_type)
    assert response.status_code == 422
    assert response.json() == {"detail": "Completed type error"}
