from fastapi import Query, APIRouter

from schemas.hotels import Hotel, HotelPatch

router = APIRouter(prefix="/hotels", tags=["Отели"])

hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"},
    {"id": 3, "title": "Мальдивы", "name": "maldivi"},
    {"id": 4, "title": "Геленджик", "name": "gelendzhik"},
    {"id": 5, "title": "Москва", "name": "moscow"},
    {"id": 6, "title": "Казань", "name": "kazan"},
    {"id": 7, "title": "Санкт-Петербург", "name": "spb"},
]

@router.get("/")
def func():
    return "HelloWorld!!!"

@router.get("",
            summary="Получение отелейй",
            description="<h1>Документация к ручке get_hotel</h1>",)
def get_hotel(
    hotel_id: int | None = Query(None, description="Айдишник"),
    title: str | None = Query(None, description="Тайтл"),
    name: str | None = Query(None, description="Нейм"),
    page: int | None = Query(1, description="Страница"),
):
    hotels_ = []
    for hotel in hotels:
        if hotel_id and hotel["id"] != hotel_id:
            continue
        if title and hotel["title"] != title:
            continue
        if name and hotel["name"] != name:
            continue
        hotels_.append(hotel)

    # global page
    if len(hotels_) > 5:
        if page == 1:
            return hotels_[0:5]
        return hotels_[page*5-5:page*5]
    else:
        return hotels_




@router.post("")
def create_hotel(
        hotel_data: Hotel
):
    global hotels
    hotels.append({"id":len(hotels)+1, "title":hotel_data.title, "name":hotel_data.name})
    return {"status" : "OK"}

@router.patch("/{hotel_id}")
def change_data(
    hotel_id : int,
    hotel_data: HotelPatch
):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            hotel["title"] = hotel_data.title
            hotel["name"] = hotel_data.name
            return {"status": "ok"}
    return {"status": "none"}
