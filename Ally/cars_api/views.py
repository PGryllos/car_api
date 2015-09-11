from django.shortcuts import render
from django.http import HttpResponse

def tenNearestCars(request, location=None):
    if request.method =="POST":
        pass

    if request.method =="GET":
        location = request.GET.get('location')

    return HttpResponse("Hello, world.")
