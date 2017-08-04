from __future__ import unicode_literals

from django.db import models
from login.models import User
from shopping.models import Item

# Create your models here.

class Basket(models.Model):
    customer = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, related_name='shopping_item', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    