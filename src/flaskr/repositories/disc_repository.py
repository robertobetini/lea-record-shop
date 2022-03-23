from google.cloud import firestore
from datetime import datetime

from ..models.disc import Disc
from ..utils.string_utils import string_is_null_or_whitespace

class DiscRepository:
    def __init__(self):
        self.__db = firestore.Client()
        self.__collection_name = u"Discs"

    def insert(self, disc: Disc):
        self \
            .__db \
            .collection(self.__collection_name) \
            .document() \
            .set(disc.to_dict())

    def get(self, style: str, year: int, artist: str, name: str, limit: int, skip: int = 0):
        disc_ref = self.__db.collection(self.__collection_name)
        
        if not string_is_null_or_whitespace(style):
            query = disc_ref.where(u"style", u"==", style)
        if year is not None:
            if year > 0:
                year_start = datetime(year, 1, 1)
                year_end = datetime(year, 12, 31)
                query = disc_ref.where(u"release_date", u">=", year_start)
                query = disc_ref.where(u"release_date", u"<=", year_end)
        if not string_is_null_or_whitespace(artist):
            query = disc_ref.where(u"artist", u"==", artist)
        if not string_is_null_or_whitespace(name):
            query = disc_ref.where(u"name", u"==", name)

        return query.offset(skip).limit(limit).stream()
