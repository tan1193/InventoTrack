from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import database
from app.db.database import SessionLocal
from . import model, crud

# Initialize the app
app = FastAPI()

# Create database tables
model.Base.metadata.create_all(bind=database.engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a product
@app.post("/products/")
def create_product(name: str, description: str, price: float, stock_quantity: int, category_id: int, db: Session = Depends(database.get_db)):
    return crud.create_product(db=db, name=name, description=description, price=price, stock_quantity=stock_quantity, category_id=category_id)

# Read all products
@app.get("/products/")
def read_products(db: Session = Depends(database.get_db)):
    return crud.get_products(db=db)

# Update a product
@app.put("/products/{product_id}")
def update_product(product_id: int, name: str, description: str, price: float, stock_quantity: int, db: Session = Depends(database.get_db)):
    return crud.update_product(db=db, product_id=product_id, name=name, description=description, price=price, stock_quantity=stock_quantity)

# Delete a product
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(database.get_db)):
    return crud.delete_product(db=db, product_id=product_id)
