from google.cloud import firestore

class OrderRepository:
    def __init__(self):
        self.__db = firestore.AsyncClient()