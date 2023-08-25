from sqlmodel import Session, select, delete
from typing import List
from src.application.infra.sqlite.models import engine, Category
from src.domain.entity.category import Category as EntityCategory
from src.domain.entity.fields import Fields as EntityFields


def create_category(name: str):
    with Session(engine) as session:
        category = Category(name=name)
        session.add(category)
        try:
            session.commit()
            return EntityCategory(id=category.id, name=category.name), False
        except:
            True, True

def get_categorys() -> List[Category]:
    with Session(engine) as session:
        list_categorys = []
        statement = select(Category)
        db_categorys = session.exec(statement).all()
        if db_categorys:
            for category in db_categorys:
                attributes = {k: v for k, v in category.__dict__.items() if k != '_sa_instance_state'}
                obj = EntityCategory(**attributes)
                obj.fields = []
                if category.fields:
                    for field in category.fields:
                        attributes = {k: v for k, v in field.__dict__.items() if k != '_sa_instance_state'}
                        obj.fields.append(EntityFields(**attributes))
                list_categorys.append(obj)
        return list_categorys
    

def update_category(category: EntityCategory, id: int):
    with Session(engine) as session:
        statement = select(Category).where(Category.id == id)
        c = session.exec(statement).first()
        c.id = category.id
        c.name = category.name
        session.add(c)
        session.commit()

def delete_category(category: EntityCategory):
    with Session(engine) as session:
        statement = select(Category).where(Category.id == category.id)
        c = session.exec(statement).first()
        session.delete(c)
        session.commit()