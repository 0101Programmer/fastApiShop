import json

from fastapi import APIRouter, Form
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


@product_page_route.get("/product_details/{session_id}/{user_id}/{product.id}/", response_class=HTMLResponse)
async def product_by_self_and_user_id_get(request: Request, session_id: str, user_id: int, product_id: int):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    product_by_id = await Product.get(id=product_id)
    return templates.TemplateResponse("product_page.html", {"request": request,
                                                            "product_by_id": product_by_id, })


@product_page_route.post("/product_details/{session_id}/{user_id}/{product_id}/", response_class=HTMLResponse)
async def product_by_self_and_user_id_post(request: Request, session_id: str, user_id: int, product_id: int,
                                           product_amount: int = Form()):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    product_by_id = await Product.get(id=product_id)
    total_orders = 0
    if user_for_check.orders:
        total_orders += max(user_for_check.orders)
        user_for_check.orders = user_for_check.orders | json.dumps({total_orders: {"product_id": product_id,
                                                                                   "product_amount": product_amount}})
    else:
        user_for_check.orders = json.dumps({total_orders: {"product_id": product_id,
                                                           "product_amount": product_amount}})
    await user_for_check.save()

    return RedirectResponse(f'/product_details/{session_id}/{user_id}/{product_id}/')
    # return templates.TemplateResponse("product_page.html", {"request": request,
    #                                                         "product_by_id": product_by_id, })
