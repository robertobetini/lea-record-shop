from repositories.customer_repository import CustomerRepository

class DiscService:
    def __init__(self, customer_repository: CustomerRepository):
        self.__customer_repository = customer_repository