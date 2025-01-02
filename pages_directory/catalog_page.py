from fastapi import APIRouter
from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from db_directory.db_models import User, Product

catalog_route = APIRouter()
templates = Jinja2Templates(directory="templates")


@catalog_route.get("/catalog/", response_class=HTMLResponse)
async def catalog(request: Request):
    all_products = await Product.all()
    return templates.TemplateResponse("catalog_page.html", {"request": request,
                                                            "all_products": all_products, })


@catalog_route.get("/catalog/{session_id}/{user_id}/", response_class=HTMLResponse)
async def catalog_by_id(request: Request, session_id: str, user_id: int):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    return templates.TemplateResponse("catalog_page.html", {"request": request,
                                                            "session_id": session_id,
                                                            "user_id": user_id})