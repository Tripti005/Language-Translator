from django.db import models

class images(models.Model):
    image = models.ImageField(upload_to='images/')
    unique_key = models.AutoField(primary_key=True)


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    hotel_Main_Img = models.ImageField(upload_to='images/')