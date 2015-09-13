from django.shortcuts import render
from django.http import JsonResponse
from cars_api.models import car
from django.contrib.gis.geos import GEOSGeometry


def tenNearestCars(request, location=None):
    if request.method == "POST":
        pass

    if request.method == "GET":
        lng, lat = str(request.GET.get('location')).split(',')

        # naive approach for knn
        query1 = """ SELECT * FROM cars_api_car cars
        ORDER BY ST_Distance(cars.lnglat, ST_PointFromText('POINT(%s %s)', 4326))
        ASC LIMIT 10 """ %(lng, lat)

        data = { "cars": [] }

    for obj in car.objects.raw(query1):
        data["cars"].append({
            "description": obj.desc,
            "latitude": obj.lnglat.x,
            "longitute": obj.lnglat.y
            })

    return JsonResponse(data)
