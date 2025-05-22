from ..db import KochORM


class Koch:

    def __init__(self, name, alter, rezepte):
        self.name = name
        self.alter = alter
        self.rezepte = rezepte
