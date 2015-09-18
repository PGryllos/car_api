from django.shortcuts import render
from django.http import JsonResponse
from cars_api.models import car
from django.contrib.gis.geos import GEOSGeometry
from django.shortcuts import render

import time

# home view
def interface(request):
    return render(request, 'cars_api/index.html')

# api view
def tenNearestCars(request, location=None):
    if request.method == "POST":
        pass

    if request.method == "GET":
        lng, lat = str(request.GET.get('location')).split(',')

        # naive approach for knn. Doesn't use Rtree indexing
        query1 = """
            SELECT
                *
            FROM
                cars_api_car cars
            ORDER BY
                ST_Distance(cars.lnglat, ST_PointFromText('POINT(%s %s)', 4326))
            ASC LIMIT 10""" %(lng, lat)

        # approach that uses Rtree indexing
        query2 = """
            SELECT
                *
            FROM
                cars_api_car cars
            ORDER BY
                cars.lnglat <->
                'SRID=4326;POINT(%s %s)'::geometry
            ASC LIMIT 10""" %(lng, lat)

        data = { "cars": [] }

        start = time.clock()
        cars = car.objects.raw(query2)
        end = time.clock()

        for obj in cars:
            data["cars"].append(
                    {
                        "description": obj.desc,
                        "longitude": obj.lnglat.x,
                        "latitude": obj.lnglat.y
                    })
            data["elapsed"] = end - start

        return JsonResponse(data)
