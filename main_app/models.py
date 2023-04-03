from django.db import models
from django.urls import reverse

class Watch(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    manufactured = models.IntegerField()
    img = models.URLField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'watch_id' : self.id})
        

# Create your models here.
