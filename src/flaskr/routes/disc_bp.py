from flask import Blueprint
from ..controllers.disc_controller import insert, get

disc_bp = Blueprint("disc_bp", __name__)

disc_bp.route("/api/discs", methods=["POST"])(insert)
disc_bp.route("/api/discs", methods=["GET"])(get)
