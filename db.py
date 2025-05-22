from typing import List, Optional
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship, sessionmaker

from sqlalchemy import create_engine

engine = create_engine("sqlite:///uni.db", echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


student_kurs_tabelle = Table(
    "student_kurs",
    Base.metadata,
    Column("student_id", Integer, ForeignKey("student.id"), primary_key=True),
    Column("kurs_id", Integer, ForeignKey("kurs.id"), primary_key=True),
)


class StudentORM(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(40))

    kurse: Mapped[List["KursORM"]] = relationship(
        secondary=student_kurs_tabelle, back_populates="studenten"
    )

    def __repr__(self):
        return f"Student(id={self.id}, name={self.name})"


class KursORM(Base):
    __tablename__ = "kurs"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))

    studenten: Mapped[List["StudentORM"]] = relationship(
        secondary=student_kurs_tabelle, back_populates="kurse"
    )

    def __repr__(self):
        return f"Kurs(id={self.id}, name={self.name})"


Base.metadata.create_all(engine)
