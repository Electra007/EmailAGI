from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float


class Base(DeclarativeBase):
    pass


class Customer(Base):

    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True)

    customer_name = Column(String)

    account_type = Column(String)

    customer_tier = Column(String)

    risk_score = Column(Float)

    complaint_history = Column(Integer)

    kyc_status = Column(String)