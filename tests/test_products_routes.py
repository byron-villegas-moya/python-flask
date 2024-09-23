import random
import pytest

from app import create_app
from app.product.service import get_products


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True
    })

    yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

def test_get_products(client):
    response = client.get("/products")
    assert response.status_code == 200

def test_get_product_by_sku(app, client):
    with app.app_context():
        product = get_products()[0]
        sku = str( product["sku"])
        response = client.get("/products/" + sku)
        assert response.status_code == 200

def test_save_product(app, client):
    with app.app_context():
        product = get_products()[0]
        product["sku"] = random.randint(2000, 3000)
        response = client.post("/products", json=product)
        assert response.status_code == 200