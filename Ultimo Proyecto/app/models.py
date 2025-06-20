from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, VARCHAR
from sqlalchemy.sql import func
from .database import Base
#Registro de Clientes
class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR(100), nullable=False)
    code = Column(VARCHAR(10), unique=True, nullable=False)
    created_at_time = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
#Registro de ordenes
class FoodOrder(Base):
    __tablename__ = "food_orders"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    food_name = Column(VARCHAR(100), nullable=False)
    created_at_time = Column(DateTime(timezone=True), nullable=False, server_default=func.now())