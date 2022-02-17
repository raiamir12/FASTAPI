from pydantic import BaseModel





class CarModel(BaseModel):
    brand: str
    model: str
    year: int
    name: str
    description: str
    price: int


class CarBrand(BaseModel):
    name: str
    description: str
    price: int