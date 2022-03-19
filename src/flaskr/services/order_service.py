from repositories.order_repository import OrderRepository

class DiscService:
    def __init__(self, order_repository: OrderRepository):
        self.__order_repository = order_repository
        