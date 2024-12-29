from fastapi import APIRouter
from fastapi import Form
from db_directory.db_models import User

user_crud_rout = APIRouter()


@user_crud_rout.get("/get_user/")
async def get_user(user_id: int):
    user_to_show = await User.get(id=user_id)
    return {"here it is": f'{user_to_show}'}


@user_crud_rout.post("/add_user/")
async def add_user(name: str = Form(), email: str = Form(), password: str = Form(), birthdate: str = Form()):
    user = User(name=name, email=email, password=password, birthdate=birthdate)
    await user.save()
    return {"message": 'user added'}


@user_crud_rout.put("/update_user/")
async def update_user(user_id: int = Form(), name: str = Form(), email: str = Form(), password: str = Form(), birthdate: str = Form(),):
    user = await User.get(id=user_id)
    user.name = name
    user.email = email
    user.password = password
    user.birthdate = birthdate
    await user.save()
    return {"message": 'user updated'}


@user_crud_rout.delete("/del_user/")
async def del_user(user_id: int = Form()):
    user_to_del = await User.get(id=user_id)
    await user_to_del.delete()
    return {"message": 'user deleted'}
