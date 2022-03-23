from flask import Blueprint

from ..controllers.customer_controller import insert, activate, deactivate

customer_bp = Blueprint("customer_bp", __name__)

customer_bp.route("/api/customers", methods=["POST"])(insert)
customer_bp.route("/api/customers/<customer_id>/activate", methods=["PUT"])(activate)
customer_bp.route("/api/customers/<customer_id>/deactivate", methods=["PUT"])(deactivate)