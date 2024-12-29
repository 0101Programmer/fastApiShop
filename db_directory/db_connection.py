from tortoise import Tortoise
from db_directory.db_config import db_password, db_user, db_name


async def connect_to_database():
    await Tortoise.init(
        db_url=f'asyncpg://{db_user}:{db_password}@127.0.0.1:5432/{db_name}',
        modules={'models': ['db_directory.db_models']}
    )
