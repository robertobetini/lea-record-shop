from flask import request, make_response, jsonify
from datetime import datetime

from ..services.disc_service import DiscService
from ..repositories.disc_repository import DiscRepository
from ..exceptions.argument_null_error import ArgumentNullError
from ..models.disc import Disc

disc_service = DiscService(DiscRepository())

def insert():
    body = dict(request.json)

    try:
        release_date = body.get("releaseDate")
        if release_date is None:
            raise ArgumentNullError("releaseDate can't be null.")

        date = datetime.strptime(release_date, "%Y-%m-%d")
        name = body.get("name")
        artist = body.get("artist")
        style = body.get("style")
        quantity = int(body.get("quantity"))
    
        disc = Disc(name, artist, date, style, quantity)
        disc_service.insert(disc)
        return make_response("ok", 201)
    except Exception as error:
        return make_response(str(error), 400)

def get():
    try:
        query_params = request.args

        year = None
        if query_params.get("year") is not None:
            year = int(query_params.get("year")) if query_params.get("year").isnumeric() else None

        limit = 20
        if query_params.get("limit") is not None:
            limit = int(query_params.get("limit")) if query_params.get("limit").isnumeric() else None

        skip = 0
        if query_params.get("skip") is not None:
            skip = int(query_params.get("skip")) if query_params.get("skip").isnumeric() else None

        style = query_params.get("style")
        artist = query_params.get("artist")
        name = query_params.get("name")
    
        discs = disc_service.get(style, year, artist, name, limit, skip)
        return make_response(jsonify([disc.to_dict() for disc in discs]), 200)
    except Exception as error:
        return make_response(str(error), 400)
