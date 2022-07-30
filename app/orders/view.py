from flask import Blueprint, jsonify, request, redirect

from app.orders.dao.orders_dao import OrdersDAO

bp_orders = Blueprint("bp_orders", __name__)
orders_dao = OrdersDAO()


@bp_orders.route("/", methods=["GET", "POST"])
def all_orders_page():
    if request.method == "GET":
        return jsonify(orders_dao.get_all()), 200, {'Content-Type': 'application/json'}

    elif request.method == "POST":
        if isinstance(request.json, list):
            orders_dao.add(request.json)
        elif isinstance(request.json, dict):
            orders_dao.add([request.json])
        return jsonify(request.json), 200, {'Content-Type': 'application/json'}


@bp_orders.route("/<int:oid>", methods=["GET", "PUT", "DELETE"])
def order_page(oid: int):
    if request.method == "GET":
        return jsonify(orders_dao.get_by_id(oid)), 200, {'Content-Type': 'application/json'}

    elif request.method == "PUT":
        if isinstance(request.json, list):
            orders_dao.update(request.json[0], oid)
        elif isinstance(request.json, dict):
            orders_dao.update(request.json, oid)
        return redirect("/orders")

    elif request.method == "DELETE":
        if orders_dao.delete(oid):
            return redirect("/orders")
        else:
            return "<p>Ошибка удаления заказа</p>"
