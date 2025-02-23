from flask import Blueprint, jsonify
from models import db, Encaissement

api = Blueprint("api", __name__)

@api.route("/encaissements", methods=["GET"])
def get_encaissements():
    encaissements = Encaissement.query.limit(5).all()
    return jsonify([e.to_dict() for e in encaissements])
