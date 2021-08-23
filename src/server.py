from typing import List
from src.schemas import schemas
from fastapi import FastAPI, Depends, status
from src.infra.sqlalchemy.repositorys.product import RepositoryProduct
from src.infra.sqlalchemy.repositorys.user import RepositoryUser
from src.infra.sqlalchemy.repositorys.shoppingCart import RepositoryShoppingCart
from src.infra.sqlalchemy.repositorys.puchaseOrder import RepositoryPuchaseOrder
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import db_create, get_db

# db_create()

app = FastAPI()

@app.get('/')
async def home():
    return { "messsage": "pagina inicial" }


# ----------- Usuarios ---------------
@app.get('/users', response_model=List[schemas.User])
async def users(db: Session = Depends(get_db)):
    get_users = RepositoryUser(db).list()
    return get_users

@app.post('/user', status_code=status.HTTP_201_CREATED, response_model=schemas.User)
async def user(user: schemas.User, db: Session = Depends(get_db)):
    created_user = RepositoryUser(db).create(user)
    return created_user


# ------------ Produtos --------------
@app.get('/products', response_model=List[schemas.Product])
async def products(db: Session = Depends(get_db)):
    get_products = RepositoryProduct(db).list()
    return get_products

@app.get('/product/{id}', response_model=schemas.Product)
async def product(id: int, db: Session = Depends(get_db)):
    get_product = RepositoryProduct(db).get(id)
    return get_product

@app.post('/product', status_code=status.HTTP_201_CREATED, response_model=schemas.Product)
async def product(product: schemas.Product, db: Session = Depends(get_db)):
    created_product = RepositoryProduct(db).create(product)
    return created_product

@app.post('/product/filter', response_model=List[schemas.Product])
async def product_filer(param_product: schemas.Product, db: Session = Depends(get_db)):
    filter_products = RepositoryProduct(db).filter(param_product.name)
    return filter_products

@app.delete('/product/{id}')
async def product(id: int, db: Session = Depends(get_db)):
    deleted_product = RepositoryProduct(db).delete(id)
    return deleted_product


# ------------- carrinho -----------------
@app.get('/shopping-cart/{user_id}', response_model=List[schemas.ShoppingCartOutput])
async def shopping_cart(user_id: int, db: Session = Depends(get_db)):
    shopping_cart = RepositoryShoppingCart(db).list(user_id)
    for item in shopping_cart:
        item.total = (item.quantity_product * item.product.price)
    return shopping_cart

@app.post('/shopping-cart', status_code=status.HTTP_201_CREATED, response_model=schemas.ShoppingCart)
async def shopping_cart(shopping_cart: schemas.ShoppingCart, db: Session = Depends(get_db)):
    shopping_cart = RepositoryShoppingCart(db).addProduct(shopping_cart)
    return shopping_cart

@app.put('/shopping-cart')
async def shopping_cart(shopping_cart: schemas.ShoppingCart, db: Session = Depends(get_db)):
    set_shopping_cart = RepositoryShoppingCart(db).edit(shopping_cart)
    return set_shopping_cart

@app.delete('/shopping-cart/{id}')
async def shopping_cart(id: int, db: Session = Depends(get_db)):
    deleted_product = RepositoryShoppingCart(db).delete(id)
    if(deleted_product):
        return { "message": "Produto excluido com sucesso" }
    return deleted_product

# -------------- pedidos ----------------
@app.get('/puchase-order', response_model=List[schemas.PuchaseOrderOutput])
async def puchase_order(db: Session = Depends(get_db)):
    puchase_order = RepositoryPuchaseOrder(db).list()
    return puchase_order

@app.post('/puchase-order', response_model=schemas.PuchaseOrderOutput)
async def puchase_order(puchase_order: schemas.PuchaseOrder, db: Session = Depends(get_db)):
    get_puchase_order = RepositoryPuchaseOrder(db).create(puchase_order)
    shopping_cart = RepositoryShoppingCart(db).resetShoppingCart(puchase_order.user_id)
    return get_puchase_order