"""empty message

Revision ID: first_data
Revises: fda6ad58bd8f
Create Date: 2022-12-09 01:52:41.209865

"""
from alembic import op
from sqlalchemy import orm
from datetime import datetime
from src.models import Cashier, Currency, Client, Deal

# revision identifiers, used by Alembic.
revision = 'first_data'
down_revision = 'fda6ad58bd8f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    client1 = Client(client_name='Артём Белый', passport='1111 222222')
    client2 = Client(client_name='Елизавета Кальбидух', passport='1234 098765')
    client3 = Client(client_name='Илья Кабушев', passport='9871 126830')
    client4 = Client(client_name='Кристина Майорова', passport='7777 133722')

    session.add_all([client1, client2, client3, client4])
    session.flush()


    cashier1 = Cashier(cashier_name='Маргарита Наумова')
    cashier2 = Cashier(cashier_name='Артур Пирожков')

    session.add_all([cashier1, cashier2])
    session.flush()

    currency1 = Currency(currency_name='Доллар', currency_rate=62)
    currency2 = Currency(currency_name='Евро', currency_rate=65)
    currency3 = Currency(currency_name='Рубль', currency_rate=1)
    currency4 = Currency(currency_name='Юань', currency_rate=8)

    session.add_all([currency1, currency2, currency3, currency4])
    session.flush()

    deal1 = Deal(deal_date=datetime(2022, 12, 9, 8, 56), sold=True, sum=10000, currency_id=currency3.id, client_id=client1.id, cashier_id=cashier1.id)
    deal2 = Deal(deal_date=datetime(2022, 11, 9, 8, 56), sold=False, sum=100, currency_id=currency1.id, client_id=client2.id, cashier_id=cashier1.id)
    deal3 = Deal(deal_date=datetime(2022, 10, 9, 8, 56), sold=False, sum=65, currency_id=currency2.id, client_id=client2.id, cashier_id=cashier2.id)
    deal4 = Deal(deal_date=datetime(2022, 9, 9, 8, 56), sold=False, sum=260, currency_id=currency4.id, client_id=client4.id, cashier_id=cashier2.id)


    session.add_all([deal1, deal2, deal3, deal4])
    session.commit()

def downgrade() -> None:
    pass
