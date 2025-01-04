from fastapi import APIRouter
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
