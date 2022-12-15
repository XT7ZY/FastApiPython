from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class BaseModel(Base):

    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):
        return f"<{type(self).__name__}(id={self.id})>" #pragma: no cover


class Client(BaseModel):
    __tablename__ = "clients"

    client_name = Column(String)
    passport = Column(String)

    deal = relationship("Deal", back_populates="client") 

class Currency(BaseModel):
    __tablename__ = "currencies"

    currency_name = Column(String)
    currency_rate = Column(Integer)
    
    deal = relationship("Deal", back_populates="currency") 

class Cashier(BaseModel):
    __tablename__ = "cashiers"

    cashier_name = Column(String)

    deal = relationship("Deal", back_populates="cashier") 


class Deal(BaseModel):
    __tablename__ = "deals"

    deal_date = Column(DateTime)
    sum = Column(Integer)
    sold = Column(Boolean)


    client_id = Column(Integer, ForeignKey("clients.id"))
    currency_id = Column(Integer, ForeignKey("currencies.id"))
    cashier_id = Column(Integer, ForeignKey("cashiers.id"))

    client = relationship("Client", back_populates="deal") 
    currency = relationship("Currency", back_populates="deal") 
    cashier = relationship("Cashier", back_populates="deal") 





