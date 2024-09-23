import pytest

from app import create_app
from app.exceptions.error_negocio_exception import ErrorNegocioException
from app.exceptions.error_tecnico_exception import ErrorTecnicoException
from app.handlers.exception_handler import handle_exception
from werkzeug.exceptions import NotFound


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app

def test_http_exception(app):
    with app.app_context():
        response = handle_exception(NotFound("asas"))
        assert response.code == 404

def test_generic_exception(app):
    with app.app_context():
        response = handle_exception(ArithmeticError())
        assert response[1] == 500

def test_error_negocio_exception(app):
    with app.app_context():
        response = handle_exception(ErrorNegocioException("error", "error"))
        assert response[1] == 409

def test_error_tecnico_exception(app):
    with app.app_context():
        response = handle_exception(ErrorTecnicoException("error", "error"))
        assert response[1] == 500