from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image_url = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
