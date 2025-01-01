from fastapi import APIRouter
from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from db_directory.db_models import User

home_route = APIRouter()
templates = Jinja2Templates(directory="templates")


@home_route.get("/", response_class=HTMLResponse)
async def home_get(request: Request):
    return templates.TemplateResponse("home_page.html", {"request": request})


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
