from sqlalchemy.orm import Session
from uuid import uuid4
from src.schemas import schemas
from src.infra.sqlalchemy.models import models
from src.infra.sqlalchemy.repositorys.shoppingCart import RepositoryShoppingCart

class RepositoryPuchaseOrder():

    def __init__(self, db: Session):
        self.db = db

    def create(self, puchase_order: schemas.PuchaseOrder):
        db_puchase_order = models.PuchaseOrder(id=str(uuid4()), total_price=puchase_order.total_price, 
                                               user_id=puchase_order.user_id)
        
        self.db.add(db_puchase_order)
        self.db.commit()
        self.db.refresh(db_puchase_order)
        
        for item in puchase_order.products:
            db_puchase_order_item = models.PuchaseOrderItem(product_id=item.id, user_id=puchase_order.user_id,
                                                            puchase_order_id=db_puchase_order.id)
        
            self.db.add(db_puchase_order_item)
            self.db.commit()
            self.db.refresh(db_puchase_order_item)
        return db_puchase_order

    def list(self):
        puchase_order = self.db.query(models.PuchaseOrder).all()
        return puchase_order