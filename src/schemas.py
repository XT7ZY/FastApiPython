from pydantic import BaseModel
from datetime import date

class DealBase(BaseModel):

    sold: bool
    deal_date: date
    sum: int


class DealCreate(DealBase):
    pass

class Deal(DealBase):

    id: int
    
    cashier_id: int
    client_id: int
    currency_id: int

    class Config:
        orm_mode = True





class ClientBase(BaseModel):

    client_name: str
    passport: str


class ClientCreate(ClientBase):
    pass

class Client(ClientBase):

    id: int
    deal: list[Deal] = []

    class Config:
        orm_mode = True




class CashierBase(BaseModel):

    cashier_name: str


class CashierCreate(CashierBase):
    pass

class Cashier(CashierBase):

    id: int
    deal: list[Deal] = []

    class Config:
        orm_mode = True





class CurrencyBase(BaseModel):

    currency_name: str
    currency_rate: int

class CurrencyCreate(CurrencyBase):
    pass

class Currency(CurrencyBase):

    id: int
    deal: list[Deal] = []

    class Config:
        orm_mode = True

