from sqlmodel import Session, select, delete
from typing import List
from src.application.infra.sqlite.models import Fields, engine
from src.domain.entity.fields import Fields as EntityFields

def create_field(field: EntityFields):
    with Session(engine) as session:
        create_field = Fields(name=field.name, type_field=field.type_field,  category_id=field.category_id)
        session.add(create_field)
        try:
            session.commit()
            field.id = create_field.id
            return field
        except:
            return False

def update_fields(field: EntityFields, id):
    with Session(engine) as session:
        statement = select(Fields).where(Fields.id == id)
        f = session.exec(statement).first()
        f.id = field.id
        f.name = field.name
        f.type_field = field.type_field
        f.category_id = field.category_id
        session.add(f)
        session.commit()


def delete_field(field: EntityFields):
    with Session(engine) as session:
        statement = select(Fields).where(Fields.id == field.id)
        f = session.exec(statement).first()
        session.delete(f)
        session.commit()