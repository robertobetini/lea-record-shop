from repositories.disc_repository import DiscRepository

class DiscService:
    def __init__(self, disc_repository: DiscRepository):
        self.__disc_repository = DiscRepository