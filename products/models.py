from django.db import models
# Create your models here.
class customuser(models.Model):
    name=models.CharField(max_length=10)
    password=models.CharField(max_length=8)
class phones(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    price = models.FloatField()
    display_size = models.CharField(max_length=50)
    battery_capacity = models.CharField(max_length=50)
    camera_resolution = models.CharField(max_length=50)
    storage_capacity = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    processor = models.CharField(max_length=50)
    os = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    image = models.CharField(max_length=100000)  # If you want to handle images as binary
    class Meta:
        db_table = 'phones'

