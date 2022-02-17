from fastapi import FastAPI
from app.resources import car_model_resource
from app.resources import car_brand_resource

def create_app():
    app = FastAPI(
        title="FastAPI Car Assigment By Amir",
        description="FastAPI Car",
        version="1.0",
        docs_url="/")


    app.include_router(
        car_model_resource.router,
        prefix="/model",
        tags=["Car Model"]
    )   
    
    app.include_router(
        car_brand_resource.router,
        prefix="/brand",
        tags=["Car Brand"]
    )   


    return app    