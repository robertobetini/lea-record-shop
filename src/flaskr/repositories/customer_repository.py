from google.cloud import firestore

class CustomerRepository:
    def __init__(self):
        self.__db = firestore.Client()