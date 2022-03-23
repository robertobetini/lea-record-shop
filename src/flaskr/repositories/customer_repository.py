from google.cloud import firestore

from ..models.customer import Customer

class CustomerRepository:
    def __init__(self):
        self.__db = firestore.Client()
        self.__collection_name = u"Customers"

    def insert(self, customer: Customer):
        self \
            .__db \
            .collection(self.__collection_name) \
            .document() \
            .set(customer.to_dict())