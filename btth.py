from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

products = [
    {"id": 1, "name": "Keyboard", "price": 500000},
    {"id": 2, "name": "Mouse", "price": 300000}
]

class Product(BaseModel):
    name: str
    price: float

@app.get("/products")
def get_products():
    return products


@app.post("/products", status_code=201)
def create_product(product: Product):

    if product.name.strip() == "":
        raise HTTPException(status_code=400, detail = "Name khong duoc rong")

    if product.price <= 0:
        raise HTTPException(status_code=400, detail = "Price phai lon hon 0")

    add_product = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price
    }

    products.append(add_product)
    return {
        'mesage': 'Them thanh cong san pham',
        'data': add_product
        }

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product["id"] == product_id:
            products.pop(index)
            return {
                "message": "Delete thanh cong"
            }
    raise HTTPException(status_code = 404, detail = "Product not found")