from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()
    brand = models.CharField(max_length=30)
    price = models.FloatField()
    gtin = models.CharField(max_length=13)
