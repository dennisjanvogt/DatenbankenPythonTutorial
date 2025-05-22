from db import KochORM, RezeptORM, ZutatORM
from sqlalchemy.orm import Session

kochi = KochORM(
    name="Hans",
    alter=74,
    rezepte=[RezeptORM(gericht="Bolognese", zutaten=[ZutatORM(name="Spaghetti")])],
)

with Session() as session:

    session.add(kochi)
    session.commit()
