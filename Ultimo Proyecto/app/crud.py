from sqlalchemy.orm import Session
from . import models, schemas

def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()

def get_client_by_code(db: Session, code: str):
    return db.query(models.Client).filter(models.Client.code == code).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()

def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(name=client.name, code=client.code)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_food_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.FoodOrder).offset(skip).limit(limit).all()

def create_food_order(db: Session, food_order: schemas.FoodOrderCreate):
    db_food_order = models.FoodOrder(**food_order.dict())
    db.add(db_food_order)
    db.commit()
    db.refresh(db_food_order)
    return db_food_order

def update_food_order(db: Session, food_order_id: int, food_order: schemas.FoodOrderUpdate):
    db_food_order = db.query(models.FoodOrder).filter(models.FoodOrder.id == food_order_id).first()
    if not db_food_order:
        return None
    
    if food_order.client_id is not None:
        db_food_order.client_id = food_order.client_id
    if food_order.food_name is not None:
        db_food_order.food_name = food_order.food_name
    
    db.commit()
    db.refresh(db_food_order)
    return db_food_order

def delete_food_order(db: Session, food_order_id: int):
    db_food_order = db.query(models.FoodOrder).filter(models.FoodOrder.id == food_order_id).first()
    if not db_food_order:
        return False
    
    db.delete(db_food_order)
    db.commit()
    return True