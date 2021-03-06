from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    comment=models.TextField()
    point=models.IntegerField(default=0)
    pic=models.ImageField(upload_to="user/%y") # /media/user/년도(월,일도 가능) 
    def getpic(self):
        if self.pic:
            return self.pic.url 
        else:
            return "/media/익명이.png"