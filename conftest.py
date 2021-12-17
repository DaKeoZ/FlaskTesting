import pytest
import app as webapp
from dbcm2 import DBcm
from appconfig import config


@pytest.fixture
def app():
    app = webapp.app
    return app


@pytest.fixture
def clean_up_db():
    yield
    with DBcm.UseDatabase(config) as db:
        SQL = """
            delete from reviews
        """
        db.execute(SQL)
