from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    tags = TaggableManager()
    
    def __str__(self):
        return self.title
    