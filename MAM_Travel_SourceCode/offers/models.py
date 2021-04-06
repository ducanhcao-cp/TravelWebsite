from django.db import models

# Create your models here.
class Tours(models.Model):
    title = models.CharField(max_length=250) 
    price = models.CharField(max_length=50)
    image = models.ImageField()
    description = models.TextField(max_length=1000)
    content = models.TextField() 
    trip_duration = models.CharField(max_length=10, default="3N2D")
    rating = models.CharField(max_length=3, default="7.0")
    review_title = models.CharField(max_length=10, default="good")
    review_number = models.CharField(max_length=5, default="10")
    def __str__(self):
        return self.title 

class tourImages(models.Model):
    tours = models.ForeignKey(Tours, default=None, on_delete=models.CASCADE) 
    images = models.FileField(upload_to = 'images/') 
    def __str__(self):
        return self.tours.title

class Deal(models.Model):
    tour = models.CharField(max_length=250) 
    name = models.CharField(max_length=50)  
    phone_number = models.CharField(max_length=15) 
    adult = models.CharField(max_length=3)
    children = models.CharField(max_length=3)
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        template = '{0.name} {0.phone_number} {0.create_at}'
        return template.format(self)