from typing import List
from db import SessionLocal, StudentORM, KursORM
from sqlalchemy import select


class Student:

    def __init__(self, name, kurse: List[KursORM] = []):
        self.name = name
        self.kurse = kurse

    def save_to_db(self):

        student = StudentORM(name=self.name, kurse=self.kurse)

        with SessionLocal() as session:
            session.add(student)
            session.commit()

    @classmethod
    def get_all(cls):
        with SessionLocal() as session:
            return session.execute(select(StudentORM)).all()
