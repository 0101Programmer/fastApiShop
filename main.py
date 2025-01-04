from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from tortoise.contrib.fastapi import register_tortoise
from crud_directory.product_crud import product_crud_rout
from crud_directory.user_crud import user_crud_rout
from db_directory.db_config import db_user, db_password, db_name
from pages_directory.catalog_page import catalog_route
from pages_directory.home_page import home_route
from pages_directory.personal_account_page import personal_account_route
from pages_directory.product_page import product_page_route
from pages_directory.reg_and_auth_page import reg_and_auth_route
from pages_directory.user_data_changing_page import user_data_changing_route

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(home_route)
app.include_router(catalog_route)
app.include_router(product_crud_rout)
app.include_router(user_crud_rout)
app.include_router(reg_and_auth_route)
app.include_router(personal_account_route)
app.include_router(user_data_changing_route)
app.include_router(product_page_route)
register_tortoise(
    app,
    db_url=f'asyncpg://{db_user}:{db_password}@127.0.0.1:5432/{db_name}',
    modules={'models': ['db_directory.db_models']},
    generate_schemas=True,
    add_exception_handlers=True,
)

