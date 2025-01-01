from fastapi import APIRouter, Form
from fastapi import Request, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from db_directory.db_models import User

user_data_changing_route = APIRouter()
templates = Jinja2Templates(directory="templates")


@user_data_changing_route.get("/user_data_changing/{session_id}/{user_id}/{data_to_change}", response_class=HTMLResponse)
async def user_data_changing_get(request: Request, session_id: str, user_id: int, data_to_change: str):

    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    return templates.TemplateResponse("user_data_changing_page.html", {"request": request,
                                                                       "session_id": session_id,
                                                                       "user_id": user_id,
                                                                       "data_to_change": data_to_change,
                                                                       "user_data": user_for_check, })


@user_data_changing_route.post("/user_data_changing/{session_id}/{user_id}/{data_to_change}", response_class=HTMLResponse)
async def user_data_changing_post(session_id: str, user_id: int, new_name: str = Form(None), new_email: str = Form(None), new_password: str = Form(None), new_repeat_password: str = Form(None)):

    user_for_check = await User.get_or_none(id=user_id, session_id=session_id)
    if not user_for_check:
        raise HTTPException(403, 'Доступ запрещён')

    if new_name:
        user_for_check.name = new_name

    elif new_email:
        is_existed_email = await User.get_or_none(email=new_email)
        if is_existed_email:
            return {f"Ошибка": "пользователь с таким email уже зарегистрирован"}
        else:
            user_for_check.email = new_email

    elif new_password:
        if new_password != new_repeat_password:
            return {f"Ошибка": "пароли не совпадают"}
        else:
            user_for_check.password = new_password

    await user_for_check.save()
    return RedirectResponse(f'/personal_account/{session_id}/{user_id}')
