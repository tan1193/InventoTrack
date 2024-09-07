from pyexpat import model
from sqlalchemy.orm import Session


# Create a new product
def create_product(db: Session, name: str, description: str, price: float, stock_quantity: int, category_id: int):
    product = model.Product(name=name, description=description, price=price, stock_quantity=stock_quantity, category_id=category_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# Read all products
def get_products(db: Session):
    return db.query(model.Product).all()

# Update a product
def update_product(db: Session, product_id: int, name: str, description: str, price: float, stock_quantity: int):
    product = db.query(model.Product).filter(model.Product.id == product_id).first()
    product.name = name
    product.description = description
    product.price = price
    product.stock_quantity = stock_quantity
    db.commit()
    return product

# Delete a product
def delete_product(db: Session, product_id: int):
    product = db.query(model.Product).filter(model.Product.id == product_id).first()
    db.delete(product)
    db.commit()
