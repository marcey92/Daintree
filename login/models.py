from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



#create user model 

class Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True)
    first_line = models.CharField(max_length=30, blank=True)
    town = models.CharField(max_length=30, blank=True)
    postcode = models.CharField(max_length=30, blank=True)

@receiver(post_save, sender=User)
def create_user_address(sender, instance, created, **kwargs):
    if created:
        Info.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_address(sender, instance, **kwargs):
    instance.info.save()

        
