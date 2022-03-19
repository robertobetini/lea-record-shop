from google.cloud import firestore

class DiscRepository:
    def __init__(self):
        self.__db = firestore.AsyncClient()