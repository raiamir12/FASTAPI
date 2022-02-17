from fastapi import status, APIRouter, Response,Path
from ..models import car
from ..dto.car import CarBrand
from bson import ObjectId
car = car.Car()


router = APIRouter() 



@router.get('/')
async def fetch_all_carbrands():     
    return car.find({})

@router.post('/add')
async def fetch_all_carbrands(carbrand: CarBrand):         
    response=car.create(dict(carbrand))
    return {"Response":response}


@router.put('/{id}')
async def update_carbrand(id:str,carbrand: CarBrand):         
    response=car.update(dict(carbrand),{"_id": ObjectId("id")})
    return {"Response":response}

@router.delete('/{id}')
async def delete_carbrands(id:str):         
    response=car.delete({"_id": ObjectId("id")})
    return {"Response":response}    

