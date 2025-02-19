from ninja import Schema
from typing import Optional
from datetime import date

class UserIn(Schema):
    username: str
    email: str
    password: str
    is_proprietario: bool = False
    is_morador: bool = False
    is_funcionario: bool = False
    telefone: Optional[str] = None
    nif: Optional[str] = None
    data_nascimento: Optional[date] = None

class UserOut(Schema):
    id: int
    username: str
    email: str
    is_proprietario: bool
    is_morador: bool
    is_funcionario: bool
    telefone: Optional[str] = None
    nif: Optional[str] = None
    data_nascimento: Optional[date] = None

class ProfileOut(Schema):
    user: UserOut
    foto_perfil: Optional[str] = None
    endereco: Optional[str] = None

class LoginIn(Schema):
    username: str
    password: str

class TokenOut(Schema):
    refresh: str
    access: str