from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryProduct():

    def __init__(self, db: Session):
        self.db = db

    def create(self, product: schemas.Product):
        db_product = models.Product(name=product.name, price=product.price,
                                    minimun=product.minimun, amount_per_package=product.amount_per_package,
                                    max_availability=product.max_availability)

        self.db.add(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def list(self):
        products = self.db.query(models.Product).all()
        return products

    def filter(self, name: str):
        products = self.db.query(models.Product).filter(models.Product.name.like(f'%{name}%')).all()
        return products

    def get(self, id: int):
        product = self.db.query(models.Product).get(id)
        return product

    def delete(self, id: int):
        product = self.get(id)
        if(product):
            self.db.delete(product)
            self.db.commit()
            return True
        
        return { "message": "Produto não encontrado" }