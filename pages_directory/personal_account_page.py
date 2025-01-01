from fastapi import APIRouter
from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from db_directory.db_models import User

personal_account_route = APIRouter()
templates = Jinja2Templates(directory="templates")


@personal_account_route.get("/personal_account/{session_id}/{user_id}", response_class=HTMLResponse)
async def personal_account_get(request: Request, session_id: str, user_id: int):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    return templates.TemplateResponse("personal_account_page.html", {"request": request,
                                                                     "session_id": session_id,
                                                                     "user_id": user_id,
                                                                     "user_data": user_for_check, })


@personal_account_route.post("/personal_account/{session_id}/{user_id}", response_class=HTMLResponse)
async def personal_account_post(request: Request, session_id: str, user_id: int):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    return templates.TemplateResponse("personal_account_page.html", {"request": request,
                                                                     "session_id": session_id,
                                                                     "user_id": user_id,
                                                                     "user_data": user_for_check, })


@personal_account_route.post("/logout/{session_id}/{user_id}", response_class=HTMLResponse)
async def logout_post(session_id: str, user_id: int):
    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    user_for_check.session_id = None
    await user_for_check.save()

    return RedirectResponse('/')
