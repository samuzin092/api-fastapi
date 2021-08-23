from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositoryUser():

    def __init__(self, db: Session):
        self.db = db

    def create(self, user: schemas.User):
        db_user = models.User(name=user.name, email=user.email, telephone=user.telephone)

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def list(self):
        users = self.db.query(models.User).all()
        return users