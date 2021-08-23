# from uuid import uuid4
from pydantic.types import UUID4
from sqlalchemy.orm import relationship

from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy import Column, Integer, String, Float
from src.infra.sqlalchemy.config.database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String())
    telephone = Column(String())

class Product(Base):

    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    minimun = Column(Integer)
    amount_per_package = Column(Integer)
    max_availability = Column(Float)

class ShoppingCart(Base):

    __tablename__ = "shopping_cart"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id', name="fk_user"))
    product_id = Column(Integer, ForeignKey('product.id', name="fk_product"))
    user = relationship("User")
    product = relationship("Product")
    quantity_product = Column(Integer)


class PuchaseOrderItem(Base):

    __tablename__ = "puchase_order_item"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('product.id', name="fk_puchase_order_product"))
    product = relationship("Product")
    user_id = Column(Integer, ForeignKey('user.id', name="fk_puchase_order_user"))
    puchase_order_id = Column(Integer, ForeignKey('puchase_order.id', name="fk_puchase_order"))

class PuchaseOrder(Base):

    __tablename__ = "puchase_order"

    id = Column(String, primary_key=True, index=True)
    total_price = Column(Float)
    user_id = Column(Integer, ForeignKey('user.id', name="fk_user"))
    user = relationship("User")
    items = relationship("PuchaseOrderItem")