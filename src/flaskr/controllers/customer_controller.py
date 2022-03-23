from flask import request, make_response, jsonify
from datetime import datetime

from ..models.customer import Customer

from ..exceptions.argument_null_error import ArgumentNullError

from ..repositories.customer_repository import CustomerRepository

from ..services.customer_service import CustomerService

customer_service = CustomerService(CustomerRepository())

def insert():
    body = dict(request.json)

    try:
        birth_date = body.get("birthDate")
        if birth_date is None:
            raise ArgumentNullError("birthDate can't be null.")

        date = datetime.strptime(birth_date, "%Y-%m-%d")
        name = body.get("name")
        email = body.get("email")
        phone = body.get("phone")
        document = body.get("document")
        
        customer = Customer(document, name, date, email, phone)

        customer_service.insert(customer)
        return make_response("ok", 201)
    except Exception as error:
        return make_response(str(error), 400)

def activate(customer_id: str):
    try:
        customer_service.activate(customer_id)
        return make_response("ok", 202)
    except Exception as error:
        return make_response(str(error), 400)

def deactivate(customer_id: str):
    try:
        customer_service.deactivate(customer_id)
        return make_response("ok", 202)
    except Exception as error:
        return make_response(str(error), 400)