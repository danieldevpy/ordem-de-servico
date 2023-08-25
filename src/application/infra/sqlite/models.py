from typing import List, Optional
from sqlmodel import Field, SQLModel, create_engine, Relationship, LargeBinary
from datetime import date


class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    fields: List["Fields"] = Relationship(back_populates="category")


class Fields(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(unique=True)
    type_field: str = Field(default='texto curto')
    category_id: int = Field(foreign_key="category.id")
    category: Optional[Category] = Relationship(back_populates="fields")


class OrderService(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    status: Optional[bool] = Field(default=True)
    data_json: Optional[str] = None
    date: str = Field(default=date.today().strftime("%d/%m/%Y"))


class Cliente(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    cel: Optional[str] = None


class Cabecalho(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    infos: Optional[str] = None
    data: Optional[bytes] = Field(LargeBinary)


engine = create_engine("sqlite:///ordem.db")

SQLModel.metadata.create_all(engine)