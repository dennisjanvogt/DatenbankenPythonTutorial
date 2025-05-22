from ..db import RezeptORM
from sqlalchemy.orm import Session


class Rezept:

    def __init__(self, name):
        self.name = name

    def save_to_db(self):
        with Session() as session:
            rezept = RezeptORM(name=self.name)

    def update_in_db(self):
        pass

    def del_from_db(self):
        pass

    @classmethod
    def get_all(cls):
        pass

    @classmethod
    def get_by_id(cls):
        pass
