from django.db import models


class Place(models.Model):
    title_place_on_map = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description_short = models.CharField(max_length=255, verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Полное описание')
    lng = models.CharField(max_length=100, verbose_name='Долгота')
    lat = models.CharField(max_length=100, verbose_name='Широта')
    
    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локации'
        ordering = ['title_place_on_map']
    
    def __str__(self):
        return self.title
    

class Image(models.Model):
    
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(verbose_name='Картинка')
    position = models.IntegerField(verbose_name='Позиция')
    
    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['position']

    def __str__(self):
        return f'{self.id} {self.place.title}'
    
