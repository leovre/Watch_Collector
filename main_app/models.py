from django.db import models

class Watch(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    manufactured = models.IntegerField()
    img = models.URLField()

    def __str__(self):
        return self.name
        

# Create your models here.
