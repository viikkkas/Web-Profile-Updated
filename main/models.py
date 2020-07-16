from django.db import models

# Create your models here.
class Profile(models.Model):
    desc = models.CharField(max_length=300)

class Training(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=300)
    img = models.ImageField(upload_to='pics')
    link = models.CharField(max_length=500)

class Projects(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics2')
    link = models.CharField(max_length=500)