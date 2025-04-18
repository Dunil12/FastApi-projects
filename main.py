from fastapi import FastAPI, Query, Body
import uvicorn
from fastapi.openapi.docs import get_swagger_ui_html

hotels = [
    {'id' : 1, 'title' : 'Sochi', "name" : "sasha"},
    {'id' : 2, 'title' : 'Dubai', "name" : "dasha"}
]

app = FastAPI()

@app.get("/")
def func():
    return "HelloWorld!!!"

@app.get("/hotelsss")
def get_hotel(
        id: int = Query(default=None, description='id hotel'),
        title: str = Query(default=None, description='название отеля'),
):
    return [hotel for hotel in hotels if hotel["title"] == title]

@app.post("/hotels")
def create_hotel(
        id: int = Body(embed=True),
        title: str = Body(embed=True)
):
    global hotels
    hotels.append({"id":id, "title":title})
    return {"status" : "OK"}

@app.patch("/hotels/{hotel_id}")
def change_data(
    hotel_id : int,# = Body(embed=True),
    title: str = Body(embed=True),
    name: str = Body(embed=True)
):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            hotel["title"] = title
            hotel["name"] = name
            return {"status": "ok"}
    return {"status": "none"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.6", port=8000, reload=True)