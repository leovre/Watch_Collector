from django.db import models
from django.urls import reverse

CLEAN = (
    ('W', 'Wipe'),
    ('B', 'Brush'),
    ('S', 'Shine'),
)


class Watch(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    manufactured = models.IntegerField()
    img = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'watch_id': self.id})


class Cleaning(models.Model):
    date = models.DateField('Cleaning Date')
    polish = models.CharField(
        max_length=1,
        choices=CLEAN,
        default=CLEAN[0][0]
    )

    watch = models.ForeignKey(Watch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_polish_display()} on {self.date}'
