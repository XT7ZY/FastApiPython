from sqlalchemy.orm import Session

from src import models, schemas


def create_client(db: Session, client: schemas.ClientCreate):

    db_client = models.Client(client_name=client.client_name, passport=client.passport)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


def create_cashier(db: Session, cashier: schemas.CashierCreate):

    db_cashier = models.Cashier(cashier_name=cashier.cashier_name)
    db.add(db_cashier)
    db.commit()
    db.refresh(db_cashier)
    return db_cashier


def create_currency(db: Session, currency: schemas.CurrencyCreate):

    db_currency = models.Currency(currency_name=currency.currency_name, currency_rate=currency.currency_rate)
    db.add(db_currency)
    db.commit()
    db.refresh(db_currency)
    return db_currency


def create_deal(db: Session, deal: schemas.DealCreate, client_id: int, currency_id: int, cashier_id: int):
 
    db_deal = models.Deal(**deal.dict(), client_id=client_id, currency_id=currency_id, cashier_id=cashier_id)
    db.add(db_deal)
    db.commit()
    db.refresh(db_deal)
    return db_deal



def get_client_by_id(db: Session, client_id: int):

    return db.query(models.Client).filter(models.Client.id == client_id).first()

def get_cashier_by_id(db: Session, cashier_id: int):

    return db.query(models.Cashier).filter(models.Cashier.id == cashier_id).first()

def get_currency_by_id(db: Session, currency_id: int):

    return db.query(models.Currency).filter(models.Currency.id == currency_id).first()

def get_deal_by_id(db: Session, deal_id: int):

    return db.query(models.Deal).filter(models.Deal.id == deal_id).first()


def get_client_by_name(db: Session, client_name: str):
    return db.query(models.Client).filter(models.Client.client_name == client_name).first()


def get_cashier_by_name(db: Session, cashier_name: str):
    return db.query(models.Cashier).filter(models.Cashier.cashier_name == cashier_name).first()

def get_currency_by_name(db: Session, currency_name: str):
    return db.query(models.Currency).filter(models.Currency.currency_name == currency_name).first()


def get_clients(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Client).offset(skip).limit(limit).all()

def get_deals(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Deal).offset(skip).limit(limit).all()

def get_currency(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Currency).offset(skip).limit(limit).all()

def get_cashiers(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Cashier).offset(skip).limit(limit).all()