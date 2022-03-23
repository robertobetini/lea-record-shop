from datetime import datetime
from .entity import Entity

class Order(Entity):
    def __init(self, customer_id: str, disc_id: str, quantity: int, date: datetime):
        self.customer_id = customer_id
        self.disc_id = disc_id
        self.quantity = quantity
        self.date = date
        