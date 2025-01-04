import json
from typing import Annotated, TypedDict
from enum import Enum
from fastapi import APIRouter, Form, Path
from db_directory.db_models import Product

product_crud_rout = APIRouter()


class Gender(str, Enum):
    male = "male"
    female = "female"

@product_crud_rout.get("/get_all_products/", tags=["Product CRUD"])
async def get_all_products():
    products_to_show = await Product.all()
    return {"here they are": f'{products_to_show}'}


@product_crud_rout.get("/get_product_by_id/", tags=["Product CRUD"])
async def get_product_by_id(product_id: int):
    product_to_show = await Product.get(id=product_id)
    return {"here it is": f'{product_to_show}'}


@product_crud_rout.post("/add_product/", tags=["Product CRUD"])
async def add_product(name: Annotated[str, Form()], description: Annotated[str, Form()],
                      price: Annotated[float, Form()], discount: Annotated[int, Form()],
                      in_stock: Annotated[int, Form()], gender: Annotated[Gender, Form(description='Gender')],
                      sizes_in_stock: Annotated[str, Form(description='{"S": 1, "M": 1, "L": 1}')],
                      ratings: Annotated[str, Form(description='None or (example): {"0": {"review": "cool", "rating": "5"}}')], img_path: Annotated[str, Form(description='/static/media/catalog_images/adidas/adidas_123.png')]):

    product = Product(name=name, description=description, price=price, discount=discount, in_stock=in_stock,
                      gender=gender, sizes_in_stock=json.dumps(sizes_in_stock), ratings=json.dumps(ratings) if ratings != "None" else json.dumps(None),
                      img_path=img_path)
    await product.save()
    return {"message": 'product added'}


@product_crud_rout.put("/update_product/", tags=["Product CRUD"])
async def update_product(product_id: int = Form(description='If any field does not change, leave the default value (0 or string)'), name: str = Form(), description: str = Form(), price: float = Form(),
                         discount: int = Form(description='If discount field does not change, leave -1 here'), in_stock: int = Form(), gender: Gender = Form(), sizes_in_stock: str = Form(),
                         ratings: str = Form(), img_path: str = Form()):
    product = await Product.get(id=product_id)
    product.name = name if name != 'string' else product.name
    product.description = description if description != 'string' else product.description
    product.price = price if price != 0 else product.price
    product.discount = discount if discount != -1 else product.discount
    product.in_stock = in_stock if in_stock != 0 else product.in_stock
    product.gender = gender if gender != 'string' else product.gender
    product.sizes_in_stock = json.dumps(sizes_in_stock) if sizes_in_stock != 'string' else product.sizes_in_stock
    product.ratings = json.dumps(ratings) if ratings != 'string' else product.ratings
    product.img_path = img_path if img_path != 'string' else product.img_path
    await product.save()
    return {"message": 'product updated'}


@product_crud_rout.delete("/del_product_by_id/", tags=["Product CRUD"])
async def del_product_by_id(product_id: int):
    product_to_del = await Product.get(id=product_id)
    await product_to_del.delete()
    return {"message": 'product deleted'}


@product_crud_rout.delete("/del_all_products/", tags=["Product CRUD"])
async def del_all_products():
    products_to_del = await Product.all()
    for product in products_to_del:
        await product.delete()
    return {"message": 'all products were deleted'}
