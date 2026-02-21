from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    cpf = Column("CPF", String, primary_key=True)
    email = Column(String)
    password = Column(String) 
    name = Column(String)

class Servico(Base):
    __tablename__ = "serviços"
    id_servico = Column("id_serviço", Integer, primary_key=True, index=True)
    name = Column(String)
    descricao = Column(String)

class Pedido(Base):
    __tablename__ = "pedidos"
    id_pedido = Column(Integer, primary_key=True, index=True)
    data_pedido = Column(String)
    valor_total = Column(Float)
    cpf_usuario = Column("CPF_fk_Usuario", String, ForeignKey("usuarios.CPF"))

class Produto(Base):
    __tablename__ = "produtos"
    id_produto = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    preco = Column(Float)

class Item_Pedido_Produto(Base):
    __tablename__ = "Item_Pedido_Produto"
    id_item = Column(Integer, primary_key=True, index=True)
    quantidade = Column("Quantidade", Integer)
    preco_unitario = Column("Preço_unitário", Float)
    id_fk_pedido = Column(Integer, ForeignKey("pedidos.id_pedido"))
    id_fk_produto = Column(Integer, ForeignKey("produtos.id_produto"))