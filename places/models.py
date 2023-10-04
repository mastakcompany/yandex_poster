from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    lng = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
    