from datetime import date

class Disc:
    def __init__(self, name: str, artist: str, release_date: date, style: str, quantity: int):
        self.name = name
        self.artist = artist
        self.release_date = release_date
        self.style = style
        self.quantity = quantity
        