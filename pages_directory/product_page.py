import datetime
import json

from fastapi import APIRouter, Form, status
from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from db_directory.db_models import User, Product

product_page_route = APIRouter()
templates = Jinja2Templates(directory="templates")


@product_page_route.get("/product_details/{product_id}/", response_class=HTMLResponse)
async def product_by_id_get(request: Request, product_id: int):
    product_by_id = await Product.get(id=product_id)
    return templates.TemplateResponse("product_page.html", {"request": request,
                                                            "product_by_id": product_by_id, })


@product_page_route.get("/product_details/{session_id}/{user_id}/{product_id}/", response_class=HTMLResponse)
async def product_by_self_and_user_id_get(request: Request, session_id: str, user_id: int, product_id: int):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    product_by_id = await Product.get(id=product_id)
    return templates.TemplateResponse("product_page.html", {"request": request,
                                                            "session_id": session_id,
                                                            "user_id": user_id,
                                                            "product_id": product_id,
                                                            "product_by_id": product_by_id, })


@product_page_route.post("/product_details/{session_id}/{user_id}/{product_id}/", response_class=HTMLResponse)
async def product_by_self_and_user_id_post(request: Request, session_id: str, user_id: int, product_id: int,
                                           product_amount: int = Form(), product_size: str = Form(), product_price: float = Form()):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    product_by_id = await Product.get(id=product_id)
    product_by_id.sizes_in_stock[f"{product_size}"] -= product_amount
    if product_by_id.sizes_in_stock[f"{product_size}"] < 0:
        return "Пожалуйста, выберите количество размера, не превышающее его остатка"
    total_orders = 1
    if user_for_check.orders:
        total_orders += int(max(user_for_check.orders, key=int))
        user_for_check.orders = json.dumps(user_for_check.orders | {total_orders: {"product_id": product_id,
                                                                                   "product_price": product_price,
                                                                                   "product_size": product_size,
                                                                                   "product_amount": product_amount,
                                                                                   "product_total": product_amount * product_price,
                                                                                   "product_name": product_by_id.name,
                                                                                   "order_status": "ordered",
                                                                                   "upd_at": str(datetime.datetime.now())[:19],
                                                                                   }})
    else:
        user_for_check.orders = json.dumps({total_orders: {"product_id": product_id,
                                                           "product_price": product_price,
                                                           "product_size": product_size,
                                                           "product_amount": product_amount,
                                                           "product_total": product_amount * product_price,
                                                           "product_name": product_by_id.name,
                                                           "order_status": "ordered",
                                                           "upd_at": str(datetime.datetime.now())[:19],
                                                           }})
    await product_by_id.save()
    await user_for_check.save()

    return RedirectResponse(url=f'/product_details/{session_id}/{user_id}/{product_id}/', status_code=status.HTTP_303_SEE_OTHER)