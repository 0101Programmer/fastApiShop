from fastapi import APIRouter

catalog_route = APIRouter()


@catalog_route.get("/catalog/")
async def catalog():
    return {"message": 'catalog page'}
