from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():

    db = SessionLocal()  #pragma: no cover
    try: #pragma: no cover
        yield db #pragma: no cover
    finally: #pragma: no cover
        db.close()#pragma: no cover


@app.get("/clients/", response_model=list[schemas.Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = crud.get_clients(db, skip=skip, limit=limit)
    return clients


@app.get("/clients/{client_id}", response_model=schemas.Client)
def read_client_by_id(client_id: int, db: Session = Depends(get_db)):

    db_client = crud.get_client_by_id(db, client_id=client_id)
    if db_client is None:
        raise HTTPException(status_code=404, detail="Такого клиента нет")
    return db_client


@app.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):

    db_client = crud.get_client_by_name(db, client_name=client.client_name)
    if db_client:
        raise HTTPException(status_code=400, detail="Клиент уже существует")
    return crud.create_client(db=db, client=client)





@app.get("/cashiers/", response_model=list[schemas.Cashier])
def read_cashiers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cashiers = crud.get_cashiers(db, skip=skip, limit=limit)
    return cashiers


@app.get("/cashiers/{cashier_id}", response_model=schemas.Cashier)
def read_cashier_by_id(cashier_id: int, db: Session = Depends(get_db)):

    db_cashier = crud.get_cashier_by_id(db, cashier_id=cashier_id)
    if db_cashier is None:
        raise HTTPException(status_code=404, detail="Такого кассира нет")
    return db_cashier


@app.post("/cashiers/", response_model=schemas.Cashier)
def create_cashier(cashier: schemas.CashierCreate, db: Session = Depends(get_db)):

    db_cashier = crud.get_cashier_by_name(db, cashier_name=cashier.cashier_name)
    if db_cashier:
        raise HTTPException(status_code=400, detail="Кассир уже существует")
    return crud.create_cashier(db=db, cashier=cashier)






@app.get("/currencies/", response_model=list[schemas.Currency])
def read_currencies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    currency = crud.get_currency(db, skip=skip, limit=limit)
    return currency


@app.get("/currencies/{currency_id}", response_model=schemas.Currency)
def read_currency_by_id(currency_id: int, db: Session = Depends(get_db)):

    db_currency = crud.get_currency_by_id(db, currency_id=currency_id)
    if db_currency is None:
        raise HTTPException(status_code=404, detail="Такой валюты нет")
    return db_currency


@app.post("/currencies/", response_model=schemas.Currency)
def create_currency(currency: schemas.CurrencyCreate, db: Session = Depends(get_db)):

    db_currency = crud.get_currency_by_name(db, currency_name=currency.currency_name)
    if db_currency:
        raise HTTPException(status_code=400, detail="Валюта уже есть")
    return crud.create_currency(db=db, currency=currency)




@app.post("/deal/{client_id}/{cashier_id}/{currency_id}/", response_model=schemas.Deal)
def create_deal(
    client_id: int, currency_id: int, cashier_id: int, deal: schemas.DealCreate, db: Session = Depends(get_db)
):

    return crud.create_deal(db=db, deal=deal, client_id=client_id, currency_id=currency_id, cashier_id=cashier_id)

@app.get("/deal/", response_model=list[schemas.Deal])
def read_deals(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    deals = crud.get_deals(db, skip=skip, limit=limit)
    return deals


@app.get("/deals/{deal_id}", response_model=schemas.Deal)
def read_deal_by_id(deal_id: int, db: Session = Depends(get_db)):

    db_deal = crud.get_deal_by_id(db, deal_id=deal_id)
    if db_deal is None:
        raise HTTPException(status_code=404, detail="Такой сделки не было")
    return db_deal