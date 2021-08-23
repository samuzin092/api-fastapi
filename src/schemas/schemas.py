from pydantic import BaseModel
from typing import List, Optional

from pydantic.types import UUID4

class User(BaseModel):
    id: Optional[int] = 0
    name: str = None
    email: str = None
    telephone: str = None

    class Config:
        orm_mode = True


class Product(BaseModel):
    id: Optional[int] = 0
    name: str = None
    price: Optional[int] = 0
    minimun: int = 0
    amount_per_package: int = 0
    max_availability: float = 0

    class Config:
        orm_mode = True

class ShoppingCart(BaseModel):
    id: Optional[int] = None
    user_id: Optional[int]
    product_id: Optional[int]
    quantity_product: int = 0
    product: Optional[Product]
    user: Optional[User]

    class Config:
        orm_mode = True

class ShoppingCartOutput(BaseModel):
    id: Optional[int] = 0
    quantity_product: int = 0
    product: Optional[Product]
    total: Optional[int] = 0

    class Config:
        orm_mode = True

class PuchaseOrderItem(BaseModel):

    id: Optional[int] = 0
    product_id: int
    user_id: int

    class Config:
        orm_mode = True

class PuchaseOrder(BaseModel):

    id: Optional[UUID4]
    total_price: float
    user_id: int 
    products: Optional[List[Product]]

    class Config:
        orm_mode = True


class PuchaseOrderItemOutput(BaseModel):
    product: Optional[Product]

    class Config:
        orm_mode = True

class PuchaseOrderOutput(BaseModel):
    id: Optional[UUID4]
    total_price: float
    user: Optional[User]
    items: Optional[List[PuchaseOrderItemOutput]]

    class Config:
        orm_mode = True