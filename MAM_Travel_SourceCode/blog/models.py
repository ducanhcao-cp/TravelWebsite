from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=300) 
    image = models.ImageField(default=None)
    description = models.TextField(max_length=1000)
    content = models.TextField() 
    create_at = models.DateTimeField(auto_now_add=True) 
    author = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    def __str__(self):
        return self.title 