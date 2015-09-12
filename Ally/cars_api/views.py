from django.shortcuts import render
from django.http import JsonResponse

def tenNearestCars(request, location=None):
    if request.method =="POST":
        pass

    if request.method =="GET":
        lat, lng = str(request.GET.get('location')).split(',')

    data = {
                "cars": [
                    {
                    "description": "test JsonResponse",
                    "latitude": lat,
                    "longitute": lng
                    }
                ]
            }
    return JsonResponse(data)
