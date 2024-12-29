from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

home_route = APIRouter()
templates = Jinja2Templates(directory="templates")


@home_route.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("home_page.html", {"request": request})
