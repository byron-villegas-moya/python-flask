from flask import jsonify, request
from app.product import bp
from app.product import service
from flask import Response


@bp.route("/products", methods=["GET"])
def get_products():
    products = service.get_products()

    return jsonify(products)

@bp.route("/products/<int:sku>", methods=["GET"])
def get_product_by_sku(sku: int):
    product = service.get_product_by_sku(sku)

    return jsonify(product)

@bp.route("/products", methods=["POST"])
def post_product():
    product = request.json

    service.save_product(product)

    return Response("", 200, mimetype="application/json")