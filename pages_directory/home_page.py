from fastapi import APIRouter
from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from db_directory.db_models import User

home_route = APIRouter()
templates = Jinja2Templates(directory="templates")


@home_route.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home_page.html", {"request": request})


@home_route.post("/home_by_id/{user_id}", response_class=HTMLResponse)
async def home_by_id_post(request: Request, user_id: int):
    session_mgr = request.state.session
    session_id = session_mgr.get_session_id()

    user_for_check = await User.get_or_none(id=user_id)
    if user_for_check:
        if session_id != user_for_check.session_id:
            raise HTTPException(403, 'Доступ запрещён')
    else:
        raise HTTPException(403, 'Доступ запрещён')

    return templates.TemplateResponse("home_page.html", {"request": request,
                                                         "user_id": user_id})


@home_route.get("/home_by_id/{user_id}", response_class=HTMLResponse)
async def home_by_id_get(request: Request, user_id: int):
    session_mgr = request.state.session
    session_id = session_mgr.get_session_id()

    user_for_check = await User.get_or_none(id=user_id)
    if user_for_check:
        if session_id != user_for_check.session_id:
            raise HTTPException(403, 'Доступ запрещён')
    else:
        raise HTTPException(403, 'Доступ запрещён')

    return templates.TemplateResponse("home_page.html", {"request": request,
                                                         "user_id": user_id})
