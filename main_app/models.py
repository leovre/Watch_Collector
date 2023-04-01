from django.db import models

class Watch(models.Model):
    brand = models.Charfield(max_length=100)
    name = models.CharField(max_length=100)
    manufactured = models.IntegerField()
    img = models.URLField()


# Create your models here.
