from django.db import models

# Create your models here.
class RegisterationModel(models.Model):
    name=models.CharField(default="",max_length=100)
    password=models.CharField(default="",max_length=100)
    email=models.CharField(default="",max_length=100)
    image=models.CharField(default="",max_length=10000)