from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^cars$', views.tenNearestCars, name='tenNearestCars'),
]
