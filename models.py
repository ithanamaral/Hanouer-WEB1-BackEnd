from sqlalchemy import Column, Integer, String
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    cpf = Column("CPF", String, primary_key=True)
    email = Column(String)
    password = Column(String) 
    name = Column(String)

class Serviços(Base):
    __tablename__ = "serviços"

    id_serviço = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    descricao = Column(String)