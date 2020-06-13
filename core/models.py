from django.db import models
from attractions.models import Attraction

# Create your models here.
class TouristSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    okay = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)

    def __str__(self):
        return self.name
