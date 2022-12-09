from pydantic import BaseModel
from typing import List, Optional


# Skema User
class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str

    class Config():
        orm_mode = True


# Skema Password
class Password(BaseModel):
    pword: str
    day: int


class ShowPassword(BaseModel):
    pword: str
    day: int

    class Config():
        orm_mode = True


# Skema Transaction
class Transaction(BaseModel):
    ordered_menus: str
    total_price: int
    date: str


class ShowTransaction(BaseModel):
    ordered_menus: str
    total_price: int
    date: str

    class Config():
        orm_mode = True


# Skema Autentikasi
class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None