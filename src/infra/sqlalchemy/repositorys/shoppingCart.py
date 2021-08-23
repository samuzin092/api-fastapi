from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from src.infra.sqlalchemy.repositorys import product

class RepositoryShoppingCart():

    def __init__(self, db: Session):
        self.db = db

    def validateQuantityProduct(self, data_product, get_product):
        if(data_product.quantity_product < get_product.minimun):
            raise HTTPException(status_code=200, detail="É necessario inserir uma quantidade de produto minimo") 
        elif(data_product.quantity_product > get_product.max_availability):
            raise HTTPException(status_code=200, detail="A quantidade adicionada ao carrinho não pode ultrapassar a quantidade em estoque") 
        return True

    def addProduct(self, data: schemas.ShoppingCart):
        get_product = product.RepositoryProduct(self.db).get(data.product_id)
        validate_product = self.validateQuantityProduct(data, get_product)
        
        if(validate_product):
            db_cart = models.ShoppingCart(user_id=data.user_id, product_id=data.product_id,
                                            quantity_product=data.quantity_product)
            self.db.add(db_cart)
            self.db.commit()
            self.db.refresh(db_cart)
            return db_cart

    def edit(self, data: schemas.ShoppingCart):
        db_cart = update(models.ShoppingCart).where(models.ShoppingCart.id == data.id).values(quantity_product=data.quantity_product)
        self.db.execute(db_cart)
        self.db.commit()
        return { "message": "Carrinho atualizado" }

    def list(self, user_id):
        shopping_cart = self.db.query(models.ShoppingCart).filter(models.ShoppingCart.user_id==user_id).all()
        return shopping_cart
    
    def delete(self, user_id):
        product = self.db.query(models.ShoppingCart).get(user_id)
        if(product):
            self.db.delete(product)
            self.db.commit()
            return True
        
        return { "message": "Produto não encontrado" }

    def resetShoppingCart(self, user_id: int):
        self.db.query(models.ShoppingCart).filter(user_id==user_id).delete()
        self.db.commit()