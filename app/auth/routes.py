from flask import current_app, jsonify, request
from app.auth import bp, service
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

@bp.route("/auth", methods=["POST"])
def post_auth():
    auth = request.json

    user = service.signin(auth)

    access_token = create_access_token(identity = user["username"])

    return jsonify(access_token = access_token, expires_in = current_app.config.get("JWT_ACCESS_TOKEN_EXPIRES"))

@bp.route("/users", methods=["GET"])
@jwt_required()
def get_users():
    current_user = get_jwt_identity()
    print(current_user)

    users = service.get_users()

    return jsonify(users)