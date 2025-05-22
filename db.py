from typing import List, Optional
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import create_engine

engine = create_engine("sqlite:///kochbuch.db", echo=True)


class Base(DeclarativeBase):
    pass


class KochORM(Base):
    __tablename__ = "koch"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))
    alter: Mapped[Optional[str]]
    rezepte: Mapped[List["RezeptORM"]] = relationship(
        back_populates="koch", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"Koch(id={self.id!r}, name={self.name!r}, alter={self.alter!r})"


class RezeptORM(Base):
    __tablename__ = "rezept"
    id: Mapped[int] = mapped_column(primary_key=True)
    gericht: Mapped[str] = mapped_column(String(100))
    zutaten: Mapped[List["ZutatORM"]] = relationship(
        back_populates="rezept", cascade="all, delete-orphan"
    )
    koch_id: Mapped[int] = mapped_column(ForeignKey("koch.id"))
    koch: Mapped["KochORM"] = relationship(back_populates="rezepte")

    def __repr__(self) -> str:
        return f"Rezept(id={self.id!r}, gericht={self.gericht!r})"


class ZutatORM(Base):
    __tablename__ = "zutat"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    rezept_id: Mapped[int] = mapped_column(ForeignKey("rezept.id"))
    rezept: Mapped["RezeptORM"] = relationship(back_populates="zutaten")

    def __repr__(self) -> str:
        return f"Zutat(id={self.id!r}, name={self.name!r})"


Base.metadata.create_all(engine)
