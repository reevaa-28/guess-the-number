from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI()

class hotel(BaseModel):
    name: str
    location: str
    rating: float
    price_per_night: float
    image:str

hotels: List[hotel] = []

@app.get("/")
def read_root():
    return {"message: Welcome to the Hotel Management System"}

@app.get("/hotels")
def get_hotels():
    return hotels

@app.post("/add-hotel")
def add_hotel(hotels: hotel):
    hotels.append(hotels)
    return {"message": "Hotel added successfully"}

@app.put("/hotel/{hotel_name}")
def update_hotel(hotel_name: str, hotels: hotel):
    for index, item in enumerate(hotels):
        if item.name == hotel_name:
            hotels[index] = hotels
            return {"message": "Hotel updated successfully"}
    return {"error": "Hotel not found"}

@app.delete("/hotel/{hotel_name}")
def delete_hotel(hotel_name: str):
    for index, item in enumerate(hotels):
        if item.name == hotel_name:
            del hotels[index]
            return {"message": "Hotel deleted successfully"}
    return {"error": "Hotel not found"}

@app.post("/image-upload")
def upload_image(image: str):
   return {"message": "Image uploaded successfully", "image": image}
