from flask import request


def test_home_up(client):
    assert client.get("/").status_code == 200


def test_about_up(client):
    assert client.get("/about").status_code == 200


def test_cv_up(client):
    assert client.get("/cv").status_code == 200


def test_interests_up(client):
    assert client.get("/interests").status_code == 200


def test_technologies_up(client):
    assert client.get("/technologies").status_code == 200


def test_comments_up(client):
    assert client.get("/comments").status_code == 200


def test_reviews_up(client):
    assert client.get("/reviews").status_code == 200


def test_missing(client):
    assert client.get("/missing").status_code == 404


def test_correct_form(client):
    response = client.get("/comments")
    assert response.status_code == 200
    assert (
        bytes('<form action="/submitted" method="post">', encoding="utf-8")
        in response.data
    )
    assert response.data.startswith(bytes("<!DOCTYPE html>", encoding="utf-8"))


def test_form_operation(client, clean_up_db):
    form_data = {
        "email": "test@test.fr",
        "comment": "Hello World",
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = client.post("/submitted", data=form_data, headers=headers)
    assert request.method == "POST"
    assert response.status_code == 200
    resp = response.data
    assert resp.startswith(bytes("<!DOCTYPE html>", encoding="utf-8"))
