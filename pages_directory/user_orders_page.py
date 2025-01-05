from fastapi import APIRouter, Form
from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from db_directory.db_models import User

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
