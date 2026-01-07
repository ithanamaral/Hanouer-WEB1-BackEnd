from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):
    _tablename_ = "usuarios"
    cpf = Column(String, primary_key=True, index=True) 
    email = Column(String, unique=True, index=True)
    password = Column(String)
    name = Column(String)

class Serviços(Base):
    _tablename_ = "serviços"

    id_serviço = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    descricao = Column(String)