from fastapi import APIRouter, Form
from fastapi import Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from db_directory.db_models import User
from pages_directory.tools_for_pages import is_adult

reg_and_auth_route = APIRouter()
templates = Jinja2Templates(directory="templates")


@reg_and_auth_route.get("/reg_and_auth_page", response_class=HTMLResponse)
async def reg_and_auth_page(request: Request):
    return templates.TemplateResponse("reg_and_auth_page.html", {"request": request})


@reg_and_auth_route.post("/reg_post")
async def reg_post(name=Form(), email=Form(), password=Form(), repeat_password=Form(),
                   birthdate=Form()):
    is_existed_email = await User.get_or_none(email=email)

    if password != repeat_password:
        return {f"Ошибка": "пароли не совпадают"}
    elif not is_adult(birthdate):
        return {f"Ошибка": "к сожалению вам нет восемнадцати лет или вы ввели некорректную дату"}
    elif is_existed_email:
        return {f"Ошибка": "пользователь с таким email уже зарегистрирован"}

    user = User(name=name, email=email, password=password, birthdate=birthdate)
    await user.save()

    new_created_user = await User.get(email=email)
    return RedirectResponse(f'/home_by_id/{new_created_user.id}')


@reg_and_auth_route.post("/log_post")
async def log_post(email=Form(), password=Form()):
    is_existed_email = await User.get_or_none(email=email)
    is_valid_password = await User.get_or_none(email=email, password=password)

    if not is_existed_email:
        return {f"Ошибка": "пользователь с таким email не зарегистрирован"}
    if not is_valid_password:
        return {f"Ошибка": "неправильный пароль"}

    authed_user = await User.get(email=email)
    await authed_user.save()
    return RedirectResponse(f'/home_by_id/{authed_user.id}')

