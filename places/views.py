from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def index(request):
    
    geojson = {
        "type"    : "FeatureCollection",
        
        "features":
            
            [
                {
                    "type"      : "Feature",
                    "geometry"  : {
                        "type"       : "Point",
                        "coordinates": [37.62, 55.793676]
                    },
                    "properties": {
                        "title"     : "«Легенды Москвы»",
                        "placeId"   : "moscow_legends",
                        "detailsUrl": reverse('place', kwargs={'place_id': 1})
                    }
                },
                {
                    "type"      : "Feature",
                    "geometry"  : {
                        "type"       : "Point",
                        "coordinates": [37.64, 55.753676]
                    },
                    "properties": {
                        "title"     : "Крыши24.рф",
                        "placeId"   : "roofs24",
                        "detailsUrl": reverse('place', kwargs={'place_id': 2})
                    }
                }
            ]
        
    }
    return render(request, 'index.html', {'places': geojson})


def get_place(requests, place_id):
    place = get_object_or_404(Place, id=place_id)
    
    place_content = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng
        }
    }
    return JsonResponse(place_content, safe=False, json_dumps_params={
        'ensure_ascii': False, 'indent': 4})

# Шаг 15 из 21
