from typing import List
from sqlmodel import Session, select, delete
from src.application.infra.sqlite.models import engine, OrderService
from src.domain.entity.order import Order

def create_order(json_data: str) -> bool:
    with Session(engine) as session:
        order = OrderService(data_json=str(json_data))
        session.add(order)
        try:
            session.commit()
            return order.id, False
        except TypeError as e:
            return False, e

def update_order(order: Order):
    with Session(engine) as session:
        statement = select(OrderService).where(OrderService.id == order.id)
        o = session.exec(statement).first()
        o.id = order.id
        o.data_json = order.data_json
        o.status = order.status
        o.date = order.date
        session.add(o)
        session.commit()

def get_orders() -> List[Order]:
    with Session(engine) as session:
        list_orders = []
        statement = select(OrderService)
        orders = session.exec(statement).all()
        if orders:
            for order in orders:
                atributos = {k: v for k, v in order.__dict__.items() if k != '_sa_instance_state'}
                obj = Order(**atributos)
                list_orders.append(obj)
        return list_orders

def get_info_orders():
    infos = {'all': None, 'open': None, 'close': None}
    with Session(engine) as session:
        statement = select(OrderService)
        infos['all'] = len(session.exec(statement).all())
        statement = select(OrderService).where(OrderService.status == True)
        infos['open'] = len(session.exec(statement).all())
        statement = select(OrderService).where(OrderService.status == False)
        infos['close'] = len(session.exec(statement).all())
        return infos