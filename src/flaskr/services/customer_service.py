from ..exceptions.argument_null_error import ArgumentNullError
from ..exceptions.invalid_email_error import InvalidEmailError
from ..exceptions.invalid_phone_error import InvalidPhoneError
from ..exceptions.invalid_document_error import InvalidDocumentError

from ..utils.string_utils import string_is_null_or_whitespace
from ..utils.email_utils import email_is_valid
from ..utils.phone_utils import phone_is_valid, remove_phone_special_characters
from ..utils.document_utils import document_is_valid, remove_document_special_characters

from ..models.customer import Customer
from ..repositories.customer_repository import CustomerRepository

class CustomerService:
    def __init__(self, customer_repository: CustomerRepository):
        self.__customer_repository = customer_repository

    def insert(self, customer: Customer) -> None:
        if customer.birth_date is None:
            raise ArgumentNullError("Customer birth date can't be null.")

        if string_is_null_or_whitespace(customer.name):
            raise ArgumentNullError("Customer name can't be null.")

        if string_is_null_or_whitespace(customer.email):
            raise ArgumentNullError("Customer email can't be null.")
        if not email_is_valid(customer.email):
            raise InvalidEmailError("Customer email must be valid.")

        if string_is_null_or_whitespace(customer.phone):
            raise ArgumentNullError("Customer phone can't be null.")
        if not phone_is_valid(customer.phone):
            raise InvalidPhoneError("Customer phone must be valid.")
        customer.phone = remove_phone_special_characters(customer.phone)

        if string_is_null_or_whitespace(customer.document):
            raise ArgumentNullError("Customer document can't be null.")
        if not document_is_valid(customer.document):
            raise InvalidDocumentError("Customer document must be valid.")
        customer.document = remove_document_special_characters(customer.document)

        if not customer.active:
            customer.active = True

        self.__customer_repository.insert(customer)

    def activate(self, customer_id: str):
        if string_is_null_or_whitespace(customer_id):
            raise ArgumentNullError("Customer Id can't be null.")

        customer = self.__customer_repository.get_by_id(customer_id)
        if customer.get("active"):
            return

        self.__customer_repository.activate(customer_id)

    def deactivate(self, customer_id: str):
        if string_is_null_or_whitespace(customer_id):
            raise ArgumentNullError("Customer Id can't be null.")

        customer = self.__customer_repository.get_by_id(customer_id)
        if not customer.get("active"):
            return
            
        self.__customer_repository.deactivate(customer_id)