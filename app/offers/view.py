from flask import Blueprint, jsonify, request, redirect

from app.offers.dao.offers_dao import OffersDAO

bp_offers = Blueprint("bp_offers", __name__)
offers_dao = OffersDAO()


@bp_offers.route("/", methods=["GET", "POST"])
def all_offers_page():
    if request.method == "GET":
        return jsonify(offers_dao.get_all()), 200, {'Content-Type': 'application/json'}

    elif request.method == "POST":
        if isinstance(request.json, list):
            offers_dao.add(request.json)
        elif isinstance(request.json, dict):
            offers_dao.add([request.json])
        return jsonify(request.json), 200, {'Content-Type': 'application/json'}


@bp_offers.route("/<int:oid>", methods=["GET", "PUT", "DELETE"])
def offer_page(oid: int):
    if request.method == "GET":
        return jsonify(offers_dao.get_by_id(oid)), 200, {'Content-Type': 'application/json'}

    elif request.method == "PUT":
        if isinstance(request.json, list):
            offers_dao.update(request.json[0], oid)
        elif isinstance(request.json, dict):
            offers_dao.update(request.json, oid)
        return redirect("/offers")

    elif request.method == "DELETE":
        if offers_dao.delete(oid):
            return redirect("/offers")
        else:
            return "<p>Ошибка удаления информации об Исполнителе</p>"
