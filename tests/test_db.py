from dbcm2 import DBcm
from appconfig import config


def test_running_locally():
    assert config["host"] == "dakeoz.fr"


def get_number_comments():
    with DBcm.UseDatabase(config) as db:
        SQL = "select count(*) from reviews"
        db.execute(SQL)
        results = db.fetchall()
    return results[0][0]


def test_add_comment(client, clean_up_db):
    initial_count = get_number_comments()
    form_data = {
        "email": "test@test.fr",
        "comment": "Hello World",
    }
    # Send the data to webapp using the FORM's URL.
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    client.post("/submitted", data=form_data, headers=headers)
    new_count = get_number_comments()
    assert new_count == initial_count + 1
