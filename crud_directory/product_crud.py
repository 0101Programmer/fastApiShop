from fastapi import APIRouter
from fastapi import Form
from db_directory.db_models import Product

product_crud_rout = APIRouter()


@product_crud_rout.get("/get_product/")
async def get_product(product_id: int):
    product_to_show = await Product.get(id=product_id)
    return {"here it is": f'{product_to_show}'}


@product_crud_rout.post("/add_product/")
async def add_product(name: str = Form(), description: str = Form(), price: float = Form(), in_stock: int = Form(), img_path: str = Form()):
    product = Product(name=name, description=description, price=price, in_stock=in_stock, img_path=img_path)
    await product.save()
    return {"message": 'product added'}


@product_crud_rout.put("/update_product/")
async def update_product(product_id: int = Form(), name: str = Form(), description: str = Form(), price: float = Form(), in_stock: int = Form(), img_path: str = Form()):
    product = await Product.get(id=product_id)
    product.name = name
    product.description = description
    product.price = price
    product.in_stock = in_stock
    product.img_path = img_path
    await product.save()
    return {"message": 'product updated'}


@product_crud_rout.delete("/del_product/")
async def del_product(product_id: int = Form()):
    product_to_del = await Product.get(id=product_id)
    await product_to_del.delete()
    return {"message": 'product deleted'}
