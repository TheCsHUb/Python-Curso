from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Client endpoints
@app.post("/clients/", response_model=schemas.Client)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db)):
    db_client = crud.get_client_by_code(db, code=client.code)
    if db_client:
        raise HTTPException(status_code=400, detail="Client code already registered")
    return crud.create_client(db=db, client=client)

@app.get("/clients/", response_model=List[schemas.Client])
def read_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    clients = crud.get_clients(db, skip=skip, limit=limit)
    return clients

# Food Order endpoints
@app.post("/food-orders/", response_model=schemas.FoodOrder)
def create_food_order(food_order: schemas.FoodOrderCreate, db: Session = Depends(get_db)):
    # Check if client exists
    db_client = crud.get_client(db, client_id=food_order.client_id)
    if not db_client:
        raise HTTPException(status_code=404, detail="Client not found")
    return crud.create_food_order(db=db, food_order=food_order)

@app.get("/food-orders/", response_model=List[schemas.FoodOrder])
def read_food_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    food_orders = crud.get_food_orders(db, skip=skip, limit=limit)
    return food_orders

@app.put("/food-orders/{food_order_id}", response_model=schemas.FoodOrder)
def update_food_order(
    food_order_id: int, 
    food_order: schemas.FoodOrderUpdate, 
    db: Session = Depends(get_db)
):
    db_food_order = crud.update_food_order(db, food_order_id=food_order_id, food_order=food_order)
    if db_food_order is None:
        raise HTTPException(status_code=404, detail="Food order not found")
    return db_food_order

@app.delete("/food-orders/{food_order_id}")
def delete_food_order(food_order_id: int, db: Session = Depends(get_db)):
    success = crud.delete_food_order(db, food_order_id=food_order_id)
    if not success:
        raise HTTPException(status_code=404, detail="Food order not found")
    return {"message": "Food order deleted successfully"}