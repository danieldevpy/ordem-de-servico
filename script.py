from datetime import datetime, timedelta
from src.application.infra.sqlite.crud_order import create_by_entity
from src.domain.entity.order import Order
from faker import Faker

fake = Faker()

# Obter a data atual
data_atual = datetime.now()

for x in range(1, 10000):
    fields = {
        "Dados do Cliente": { "Nome Completo": fake.name(),  "Celular": str(fake.phone_number())},
        "Texto aleatorio": {"Texto": fake.text()}
        }
    date_ = data_atual + timedelta(days=x)
    obj = Order(id=x, data_json= fields, status=True, date=date_.strftime("%d/%m/%Y"))
    create_by_entity(obj)