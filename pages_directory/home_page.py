from fastapi import APIRouter
from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from db_directory.db_models import User, Product

home_route = APIRouter()
templates = Jinja2Templates(directory="templates")


@home_route.get("/", response_class=HTMLResponse)
async def home_get(request: Request):
    products_per_page = 8
    products_box = []
    products_with_discount = await Product.filter(discount__not_isnull=True)
    for i in products_with_discount:
        if len(products_box) < products_per_page:
            products_box.append(i)
    return templates.TemplateResponse("home_page.html", {"request": request, "products_box": products_box})


@home_route.post("/", response_class=HTMLResponse)
async def home_post(request: Request):
    return templates.TemplateResponse("home_page.html", {"request": request})


@home_route.post("/home_by_id/{session_id}/{user_id}", response_class=HTMLResponse)
async def home_by_id_post(request: Request, session_id: str, user_id: int):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    return templates.TemplateResponse("home_page.html", {"request": request,
                                                         "session_id": session_id,
                                                         "user_id": user_id})


@home_route.get("/home_by_id/{session_id}/{user_id}", response_class=HTMLResponse)
async def home_by_id_get(request: Request, session_id: str, user_id: int):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    return templates.TemplateResponse("home_page.html", {"request": request,
                                                         "session_id": session_id,
                                                         "user_id": user_id})


@home_route.get("/contacts", response_class=HTMLResponse)
async def about_us_get(request: Request):
    return templates.TemplateResponse("about_us_page.html", {"request": request})


@home_route.get("/contacts_by_id/{session_id}/{user_id}", response_class=HTMLResponse)
async def about_us_by_id_get(request: Request, session_id: str, user_id: int):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    return templates.TemplateResponse("about_us_page.html", {"request": request,
                                                        "session_id": session_id,
                                                        "user_id": user_id})
