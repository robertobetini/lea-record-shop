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

    def get_by_id(self, customer_id: str):
        return self \
        .__db \
        .collection(self.__collection_name) \
        .document(customer_id) \
        .get() \
        .to_dict()

    def activate(self, customer_id: str):
        self \
        .__db \
        .collection(self.__collection_name) \
        .document(customer_id) \
        .update({u"active": True})
    
    def deactivate(self, customer_id: str):
        self \
        .__db \
        .collection(self.__collection_name) \
        .document(customer_id) \
        .update({u"active": False}) 