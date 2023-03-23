from django.db import models
from django.contrib.auth.models import AbstractUser


from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    profession = models.CharField(max_length=100)
    phone_number=models.CharField(max_length=15,unique=True)
    activity_choices = (("on","online"),("off","offline"),("last seen recently","last seen recently"))
    activity_status = models.CharField(max_length=20, choices=activity_choices,default="off")

class Info(models.Model):
    profile = models.OneToOneField(Profile,on_delete=models.CASCADE, related_name="info")
    consultation_fee = models.IntegerField(default =200)
    meeting_time = models.IntegerField(default=15)
    wallet = models.IntegerField(default=2000)

# class Room(models.Model):
#     profile = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="rooms")
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True)


# class Message(models.Model):
#     room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
#     user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
#     content = models.TextField()
#     date_added = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ('date_added',)