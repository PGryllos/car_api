from django.contrib.gis.db import models

# The car model. Every row represents a car using its position
class cars(models.Model):
    # overriding default manager with GeoManager
    objects = models.GeoManager()

    lnglat = models.PointField(srid=4326)   # position of the car
    desc = models.CharField(max_length=80)  # description of the area
