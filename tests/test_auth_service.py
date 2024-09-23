import pytest

from app import create_app
from app.auth.service import get_users, signin
from werkzeug.exceptions import Unauthorized

@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app

def test_signin(app):
    with app.app_context():
        auth = dict()
        auth["username"] = "byron.villegas"
        auth["password"] = "admin123"

        users = signin(auth)

        assert users is not None

def test_signin_whithout_username(app):
    with app.app_context():
        with pytest.raises(Unauthorized):
            auth = dict()
            auth["username"] = ""
            auth["password"] = "admin123"

            signin(auth)

def test_signin_whithout_password(app):
    with app.app_context():
        with pytest.raises(Unauthorized):
            auth = dict()
            auth["username"] = "byron.villegas"
            auth["password"] = ""

            signin(auth)


def test_signin_not_exist(app):
    with app.app_context():
        with pytest.raises(Unauthorized):
            auth = dict()
            auth["username"] = "byron"
            auth["password"] = "admin321"

            signin(auth)

def test_get_users(app):
    with app.app_context():
        users = get_users()

        assert users is not None