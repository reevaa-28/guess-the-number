from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

add=FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float
    category: str

products: List[Product] = []

@add.get("/")
def read_root():
    return {"message: Welcome to the Amazon"}

@add.get("/products")
def get_products():
    return products

@add.post("/add-product")
def add_product(product: Product):
    products.append(product)
    return {"message": "Product added success"
    "fully", "product": product}

@add.put("/product/{product_id}")
def update_product(product_id: int, product: Product):
    for index, item in enumerate(products):
        if item.id == product_id:
            products[index] = product
            return {"message": "Product updated successfully"}
    return {"error": "Product not found"}

