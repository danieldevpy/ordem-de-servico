from sqlmodel import Session, select, delete
from typing import List
from src.application.infra.sqlite.models import engine, Cliente
from src.domain.entity.cliente import Cliente as Entity


def add_cliente(cliente: Entity):
    cliente = Cliente(id=cliente.id, name=cliente.name, cel=cliente.cel)
    with Session(engine) as session:
        session.add(cliente)
        session.commit()

def update_cliente(cliente: Entity):
    with Session(engine) as session:
        statement = select(Cliente).where(Cliente.id == cliente.id)
        db_cliente = session.exec(statement).first()
        db_cliente.name = cliente.name
        db_cliente.cel = cliente.cel
        session.add(db_cliente)
        session.commit()

def add_cliente_fields(name: str, cel:str) -> Entity:
    cliente = Cliente(name=name, cel=cel)
    with Session(engine) as session:
        session.add(cliente)
        session.commit()
        return Entity(id=cliente.id, name=cliente.name, cel=cliente.cel)

def get_clientes() -> List[Cliente]:
    with Session(engine) as session:
        list_clientes = []
        statement = select(Cliente)
        db_clientes = session.exec(statement).all()
        if db_clientes:
            for cliente in db_clientes:
                atributos = {k: v for k, v in cliente.__dict__.items() if k != '_sa_instance_state'}
                obj = Entity(**atributos)
                list_clientes.append(obj)
        return list_clientes
    
def del_cliente(cliente: Cliente):
    with Session(engine) as session:
        statement = select(Cliente).where(Cliente.id == cliente.id)
        db_cliente = session.exec(statement).first()
        try:
            session.delete(db_cliente)
            session.commit()
            return True
        except:
            return False