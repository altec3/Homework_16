from flask import Blueprint, jsonify, request, redirect

from app.users.dao.users_dao import UsersDAO

bp_users = Blueprint("bp_users", __name__)
users_dao = UsersDAO()


@bp_users.route("/", methods=["GET", "POST"])
def all_users_page():
    if request.method == "GET":
        return jsonify(users_dao.get_all()), 200, {'Content-Type': 'application/json'}

    elif request.method == "POST":
        if isinstance(request.json, list):
            users_dao.add(request.json)
        elif isinstance(request.json, dict):
            users_dao.add([request.json])
        return jsonify(request.json), 200, {'Content-Type': 'application/json'}


@bp_users.route("/<int:uid>", methods=["GET", "PUT", "DELETE"])
def user_page(uid: int):
    if request.method == "GET":
        return jsonify(users_dao.get_by_id(uid)), 200, {'Content-Type': 'application/json'}

    elif request.method == "PUT":
        if isinstance(request.json, list):
            users_dao.update(request.json[0], uid)
        elif isinstance(request.json, dict):
            users_dao.update(request.json, uid)
        return redirect("/users")

    elif request.method == "DELETE":
        if users_dao.delete(uid):
            return redirect("/users")
        else:
            return "<p>Ошибка удаления пользователя</p>"
