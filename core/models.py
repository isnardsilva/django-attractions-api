from django.db import models
from attractions.models import Attraction
from comments.models import Comment
from reviews.models import Review
from addresses.models import Address

# Create your models here.
class TouristSpot(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    okay = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Attraction)
    comments = models.ManyToManyField(Comment)
    reviews = models.ManyToManyField(Review)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='core', null=True, blank=True)

    def __str__(self):
        return self.name
