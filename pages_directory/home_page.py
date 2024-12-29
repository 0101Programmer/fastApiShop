from fastapi import APIRouter

home_route = APIRouter()

@home_route.get("/home/")
async def home():
    return {"message": 'home page'}