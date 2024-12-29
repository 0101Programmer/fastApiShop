from fastapi import FastAPI, Request, HTTPException, Path
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from db_directory.db_config import db_user, db_password, db_name
from db_directory.db_models import User
from tortoise.contrib.fastapi import register_tortoise
from pages_directory.home_page import home_route

from pages_directory.catalog_page import catalog_route

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(home_route)
app.include_router(catalog_route)

register_tortoise(
    app,
    db_url=f'asyncpg://{db_user}:{db_password}@127.0.0.1:5432/{db_name}',
    modules={'models': ['db_directory.db_models']},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("home_page.html", {"request": request})


@app.get("/test/")
async def test():
    user = await User.create(name='Joe', email='j@mail.ru', password='12345')
    print(user)
    return {"message": 'ok'}
