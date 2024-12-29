from fastapi import FastAPI
from db_directory.db_config import db_user, db_password, db_name
from db_directory.db_models import User
from tortoise.contrib.fastapi import register_tortoise
from pages_directory.home_page import home_route
from pages_directory.catalog_page import catalog_route


app = FastAPI()
app.include_router(home_route)
app.include_router(catalog_route)


register_tortoise(
    app,
    db_url=f'asyncpg://{db_user}:{db_password}@127.0.0.1:5432/{db_name}',
    modules={'models': ['db_directory.db_models']},
    generate_schemas=True,
    add_exception_handlers=True,
)


@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}


@app.get("/test/")
async def test():
    user = await User.create(name='Joe', email='j@mail.ru', password='12345')
    print(user)
    return {"message": 'ok'}
