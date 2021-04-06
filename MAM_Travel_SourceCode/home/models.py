from django.db import models 
from offers.models import Tours

# Create your models here.
class Special(models.Model):
    image = models.ImageField()
    tours = models.ForeignKey(Tours, default=None, on_delete=models.CASCADE) 
    def __str__(self):
        return self.tours.title
