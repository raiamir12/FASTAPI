from fastapi import status, APIRouter, Response,Path
from ..models import car
from ..dto.car import CarModel
from bson import ObjectId
car = car.Car()


router = APIRouter() 



@router.get('/')
async def fetch_all_carbrands():     
    return car.find({})

@router.get('/searchByKeywords')
async def fetch_all_carbrands(keywword:str):     
    return car.find({
  '$or': [
    {
      "brand": { "$regex": ".*"+keywword+".*"}
    },
    {
      "name": { "$regex":  ".*"+keywword+".*"}
    },
    {
      "model": { "$regex":  ".*"+keywword+".*"}
    }
    ,
    {
      "description": { "$regex":  ".*"+keywword+".*"}
    }
  ]
})


@router.get('/searchByBrand')
async def fetch_all_carbrands(brandName:str):     
    return car.find({"brand": brandName})



@router.post('/add')
async def fetch_all_carbrands(carbrand: CarModel):         
    response=car.create(dict(carbrand))
    return {"Response":response}


@router.put('/{id}')
async def update_carbrand(id:str,carbrand: CarModel):         
    response=car.update(dict(carbrand),{"_id": ObjectId("id")})
    return {"Response":response}

@router.delete('/{id}')
async def delete_carbrands(id:str):         
    response=car.delete({"_id": ObjectId("id")})
    return {"Response":response}    

        