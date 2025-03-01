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
    products_per_page = 8
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

    return templates.TemplateResponse("catalog_paginator_page.html", {"request": request,
                                                                      "products_per_page": products_per_page,
                                                                      "page_number": page_number,
                                                                      "available_pages": available_pages,
                                                                      "split_products_lists": split_products_lists, })


@catalog_route.get("/catalog/{session_id}/{user_id}/", response_class=HTMLResponse)
async def catalog_by_user_id_get(request: Request, session_id: str, user_id: int):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    split_products_lists = None
    products_per_page = 8
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
                                                            "all_products": all_products,
                                                            "session_id": session_id,
                                                            "user_id": user_id})


@catalog_route.get("/catalog/{session_id}/{user_id}/paginator/{products_per_page}/{page_number}/",
                   response_class=HTMLResponse)
async def catalog_paginator_by_user_id_get(request: Request, session_id: str, user_id: int, products_per_page: int,
                                           page_number: int):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    available_pages = []
    all_products = await Product.all()
    split_products_lists = nested_lists_maker(all_products, products_per_page)
    for i, val in enumerate(split_products_lists):
        available_pages.append(i)

    return templates.TemplateResponse("catalog_paginator_page.html", {"request": request,
                                                                      "products_per_page": products_per_page,
                                                                      "page_number": page_number,
                                                                      "available_pages": available_pages,
                                                                      "split_products_lists": split_products_lists,
                                                                      "session_id": session_id,
                                                                      "user_id": user_id})


@catalog_route.get("/catalog_filter_by_gender/{gender}/", response_class=HTMLResponse)
async def catalog_gender_filter_get(request: Request, gender: str):
    split_products_lists = None
    products_per_page = 8
    page_number = 0
    available_pages = []

    filtered_products = await Product.filter(gender=gender)
    if len(filtered_products) > products_per_page:
        split_products_lists = nested_lists_maker(filtered_products, products_per_page)
        for i, val in enumerate(split_products_lists):
            available_pages.append(i)

    return templates.TemplateResponse("catalog_by_gender_page.html", {"request": request,
                                                                      "split_products_lists": split_products_lists,
                                                                      "products_per_page": products_per_page,
                                                                      "available_pages": available_pages,
                                                                      "page_number": page_number,
                                                                      "gender": gender,
                                                                      "filtered_products": filtered_products, })


@catalog_route.get("/catalog/{session_id}/{user_id}/catalog_filter_by_gender/{gender}/", response_class=HTMLResponse)
async def catalog_gender_filter_by_user_id_get(request: Request, session_id: str, user_id: int, gender: str):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    split_products_lists = None
    products_per_page = 8
    page_number = 0
    available_pages = []

    filtered_products = await Product.filter(gender=gender)
    if len(filtered_products) > products_per_page:
        split_products_lists = nested_lists_maker(filtered_products, products_per_page)
        for i, val in enumerate(split_products_lists):
            available_pages.append(i)

    return templates.TemplateResponse("catalog_by_gender_page.html", {"request": request,
                                                                      "split_products_lists": split_products_lists,
                                                                      "products_per_page": products_per_page,
                                                                      "available_pages": available_pages,
                                                                      "page_number": page_number,
                                                                      "gender": gender,
                                                                      "filtered_products": filtered_products,
                                                                      "session_id": session_id,
                                                                      "user_id": user_id})


@catalog_route.get("/catalog/paginator/{products_per_page}/{page_number}/{gender}/", response_class=HTMLResponse)
async def catalog_paginator_by_gender_get(request: Request, products_per_page: int, page_number: int, gender: str):
    available_pages = []

    filtered_products = await Product.filter(gender=gender)
    split_products_lists = nested_lists_maker(filtered_products, products_per_page)
    for i, val in enumerate(split_products_lists):
        available_pages.append(i)

    return templates.TemplateResponse("catalog_paginator_by_gender_page.html", {"request": request,
                                                                                "products_per_page": products_per_page,
                                                                                "page_number": page_number,
                                                                                "available_pages": available_pages,
                                                                                "gender": gender,
                                                                                "split_products_lists": split_products_lists, })


@catalog_route.get("/catalog/paginator/{session_id}/{user_id}/{products_per_page}/{page_number}/{gender}/",
                   response_class=HTMLResponse)
async def catalog_paginator_by_gender_by_user_id_get(request: Request, session_id: str, user_id: int,
                                                     products_per_page: int, page_number: int, gender: str):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    available_pages = []
    filtered_products = await Product.filter(gender=gender)
    split_products_lists = nested_lists_maker(filtered_products, products_per_page)
    for i, val in enumerate(split_products_lists):
        available_pages.append(i)

    return templates.TemplateResponse("catalog_paginator_by_gender_page.html", {"request": request,
                                                                                "products_per_page": products_per_page,
                                                                                "page_number": page_number,
                                                                                "available_pages": available_pages,
                                                                                "gender": gender,
                                                                                "split_products_lists": split_products_lists,
                                                                                "session_id": session_id,
                                                                                "user_id": user_id})
