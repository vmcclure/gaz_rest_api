from django.db import models


class Deviation(models.Model):
    region = models.TextField()
    object_id = models.TextField()
    product_id = models.TextField()
    shift_number = models.TextField()
    shiftbegt = models.DateTimeField()
    shiftendt = models.DateTimeField()
    shipment = models.IntegerField()
    reception = models.IntegerField()
    deviation = models.IntegerField()
    version = models.IntegerField()
