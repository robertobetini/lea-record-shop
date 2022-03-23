from ..exceptions.argument_null_error import ArgumentNullError
from ..exceptions.invalid_quantity_error import InvalidQuantityError
from ..exceptions.invalid_year_error import InvalidYearError
from ..models.disc import Disc
from ..repositories.disc_repository import DiscRepository
from ..utils.string_utils import string_is_null_or_whitespace

class DiscService:
    def __init__(self, disc_repository: DiscRepository):
        self.__disc_repository = disc_repository

    def insert(self, disc: Disc):
        if disc is None:
            raise ArgumentNullError()
        if string_is_null_or_whitespace(disc.artist):
            raise ArgumentNullError("Disc artist can't be null.")
        if string_is_null_or_whitespace(disc.name):
            raise ArgumentNullError("Disc name can't be null.")
        if string_is_null_or_whitespace(disc.style):
            raise ArgumentNullError("Disc style can't be null.")
        if disc.quantity < 1:
            raise InvalidQuantityError("Disc quantity must be greater than 0.")
            
        self.__disc_repository.insert(disc)

    def get(self, style: str, year: int, artist: str, name: str, limit: int = 20, skip: int = 0):
        if year is not None:
            if year <= 0:
                raise InvalidYearError(f"Disc year '{year}' is invalid.")

        return self.__disc_repository.get(style, year, artist, name, limit, skip)