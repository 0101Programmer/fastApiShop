from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

home_route = APIRouter()
templates = Jinja2Templates(directory="templates")


@home_route.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home_page.html", {"request": request})


@home_route.post("/home_by_id/{user_id}", response_class=HTMLResponse)
async def home_by_id(request: Request, user_id: int):
    return templates.TemplateResponse("home_page.html", {"request": request,
                                                         "user_id": user_id})
