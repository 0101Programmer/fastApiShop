import datetime
import json

from fastapi import APIRouter, Form, status
from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from db_directory.db_models import User, Product

user_orders_route = APIRouter()
templates = Jinja2Templates(directory="templates")


@user_orders_route.get("/user_orders/{session_id}/{user_id}", response_class=HTMLResponse)
async def all_user_orders_get(request: Request, session_id: str, user_id: int):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    return templates.TemplateResponse("all_user_orders_page.html", {"request": request,
                                                                    "session_id": session_id,
                                                                    "user_id": user_id,
                                                                    "user_data": user_for_check, })


@user_orders_route.get("/user_orders/change_order_status/{session_id}/{user_id}/{order_id}",
                       response_class=HTMLResponse)
async def change_order_status_get(request: Request, session_id: str, user_id: int, order_id: str):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    return templates.TemplateResponse("user_order_changing_page.html", {"request": request,
                                                                        "session_id": session_id,
                                                                        "user_id": user_id,
                                                                        "order_id": order_id,
                                                                        "user_data": user_for_check, })


@user_orders_route.post("/user_orders/change_order_status/{session_id}/{user_id}/{order_id}",
                        response_class=HTMLResponse)
async def change_order_status_post(request: Request, session_id: str, user_id: int, order_id: str,
                                   new_order_status: str = Form()):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    if new_order_status == "confirm":
        return RedirectResponse(url=f'/order_confirmation/{session_id}/{user_id}/{order_id}',
                                status_code=status.HTTP_303_SEE_OTHER)
    else:
        product_by_id = await Product.get(id=user_for_check.orders[order_id]["product_id"])

        product_by_id.sizes_in_stock[user_for_check.orders[order_id]["product_size"]] += \
            user_for_check.orders[order_id]["product_amount"]

        user_for_check.orders[order_id]["order_status"] = "canceled"
        user_for_check.orders[order_id]["upd_at"] = str(datetime.datetime.now())[:19]

        await product_by_id.save()
        await user_for_check.save()

        return RedirectResponse(url=f'/user_orders/{session_id}/{user_id}/',
                                status_code=status.HTTP_303_SEE_OTHER)


@user_orders_route.get("/order_confirmation/{session_id}/{user_id}/{order_id}",
                       response_class=HTMLResponse)
async def order_confirmation_get(request: Request, session_id: str, user_id: int, order_id: str):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    return templates.TemplateResponse("order_confirmation_page.html", {"request": request,
                                                                       "session_id": session_id,
                                                                       "user_id": user_id,
                                                                       "order_id": order_id,
                                                                       "user_data": user_for_check, })


@user_orders_route.post("/order_confirmation/{session_id}/{user_id}/{order_id}",
                        response_class=HTMLResponse)
async def order_confirmation_post(request: Request, session_id: str, user_id: int, order_id: str):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    user_for_check.orders[order_id]["order_status"] = "confirmed"
    user_for_check.orders[order_id]["upd_at"] = str(datetime.datetime.now())[:19]
    await user_for_check.save()

    return RedirectResponse(url=f'/user_orders/{session_id}/{user_id}/',
                            status_code=status.HTTP_303_SEE_OTHER)
