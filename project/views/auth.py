from flask import request
from flask_restx import abort, Namespace, Resource
from project.tools.security import login_user, refresh_user_token
from project.services.users_service import UserService
from project.setup_db import db
from project.exceptions import ItemNotFound

auth_ns = Namespace('auth')

@auth_ns.route('/login')
class AuthView(Resource):
    def post(self):
        req_json = request.json
        if not req_json:
            abort(400, message="Bad request")
        try:
            user = UserService(db.session).get_item_by_email(email=req_json.get("email"))
            tokens = login_user(request.json, user)
            return tokens, 200
        except ItemNotFound:
            abort(401, message="Authorization Error")

    def put(self):
        req_json = request.json
        if not req_json:
            abort(400, message="Bad request")
        try:
            tokens = refresh_user_token(req_json)
            return tokens, 200
        except ItemNotFound:
            abort(401, message="Authorization Error")


@auth_ns.route('/register')
class AuthRegisterView(Resource):
    def post(self):
        req_json = request.json
        if "email" in req_json:
            u1 = UserService(db.session).get_item_by_email(email = req_json["email"])
            return UserService(db.session).create(req_json)
        if not req_json:
            abort(400, message="Bad request")
        return "", 404