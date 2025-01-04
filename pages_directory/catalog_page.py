from fastapi import APIRouter
from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pages_directory.tools_for_pages import nested_lists_maker
from db_directory.db_models import User, Product

catalog_route = APIRouter()
templates = Jinja2Templates(directory="templates")


@catalog_route.get("/catalog/", response_class=HTMLResponse)
async def catalog_get(request: Request):
    split_products_lists = None
    products_per_page = 6
    page_number = 0
    available_pages = []

    all_products = await Product.all()
    if len(all_products) > products_per_page:
        split_products_lists = nested_lists_maker(all_products, products_per_page)
        for i, val in enumerate(split_products_lists):
            available_pages.append(i)

    return templates.TemplateResponse("catalog_page.html", {"request": request,
                                                            "split_products_lists": split_products_lists,
                                                            "products_per_page": products_per_page,
                                                            "available_pages": available_pages,
                                                            "page_number": page_number,
                                                            "all_products": all_products, })


@catalog_route.get("/catalog/paginator/{products_per_page}/{page_number}/", response_class=HTMLResponse)
async def catalog_paginator_get(request: Request, products_per_page: int, page_number: int):
    available_pages = []

    all_products = await Product.all()
    split_products_lists = nested_lists_maker(all_products, products_per_page)
    for i, val in enumerate(split_products_lists):
        available_pages.append(i)

    return templates.TemplateResponse("catalog_page.html", {"request": request,
                                                            "products_per_page": products_per_page,
                                                            "page_number": page_number,
                                                            "available_pages": available_pages,
                                                            "split_products_lists": split_products_lists, })


@catalog_route.get("/catalog/{session_id}/{user_id}/", response_class=HTMLResponse)
async def catalog_by_user_id_get(request: Request, session_id: str, user_id: int):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    return templates.TemplateResponse("catalog_page.html", {"request": request,
                                                            "session_id": session_id,
                                                            "user_id": user_id})


@catalog_route.get("/catalog_filter_by_gender/{gender}/", response_class=HTMLResponse)
async def catalog_gender_filter_get(request: Request, gender: str):
    filtered_products = await Product.filter(gender=gender)

    return templates.TemplateResponse("catalog_by_gender_page.html", {"request": request,
                                                                      "gender": gender,
                                                                      "filtered_products": filtered_products, })
