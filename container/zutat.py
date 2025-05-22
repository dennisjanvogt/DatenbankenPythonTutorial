from db import ZutatORM
from sqlalchemy.orm import Session


class Zutat:

    def __init__(self, name):
        self.name = name

    def save_to_db(self):
        with Session() as session:
            zutat = ZutatORM(name=self.name)

            session.add(zutat)
            session.commit()

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
