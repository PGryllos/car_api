# This a very simple script that uses 'data.json' to populate the data base
# making entries for the car model

# This is a development level solution and shouldn't be used with a large file.
# If used with a file which size is comparatively close the the size of the
# memory it may cause trouble and it will surely have very slow performance.
# A better solution could be reading and processing only parts of the file at
# the time and not the whole file at once.
import json

from django.core.management.base import BaseCommand
from cars_api.models import car
from django.contrib.gis.geos import GEOSGeometry

class Command(BaseCommand):

    help = 'Run this script to populate the database with entries of cars'

    def _insert_cars(self):
        with open('../data.json') as data_file:    
            data = json.load(data_file)
     
        for entry in data["locations"]:
            lat = entry["latitude"]
            lng = entry["longitude"]
            desc = entry["description"]
     
            point = 'POINT(' + str(lng) + " " + str(lat) + ')' # just hack-ish
     
            obj = car(desc=desc, lnglat=GEOSGeometry(point)) # create car obj
            obj.save() # save to car table

    def handle(self, *args, **options):
        self._insert_cars()

