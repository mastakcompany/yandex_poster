from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.CharField(max_length=255)
    description_long = models.TextField()
    lng = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    

class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField()

    def __str__(self):
        return f'{self.id} {self.place.title}'
    
