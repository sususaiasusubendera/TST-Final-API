from sqlalchemy import Column, ForeignKey, Integer, String, Date
from .database import Base
from sqlalchemy.orm import relationship


class Password(Base):
    __tablename__ = 'passwords'
    id = Column(Integer, primary_key=True, index=True)
    pword = Column(String)
    day = Column(Integer)

    transaction = relationship("Transaction", back_populates="pword")


class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, index=True)
    ordered_menus = Column(String)
    total_price = Column(Integer)
    date = Column(String)
    pword_avail = Column(Integer, ForeignKey('passwords.pword'))

    pword = relationship("Password", back_populates="transaction")


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)