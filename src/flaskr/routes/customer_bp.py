from flask import Blueprint

from ..controllers.customer_controller import insert

customer_bp = Blueprint("customer_bp", __name__)

customer_bp.route("/api/customers", methods=["POST"])(insert)