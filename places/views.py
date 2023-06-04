from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse

from .models import Places, Images

def index(request):
    places_geo_json = {
        'type': 'FeatureCollection',
        'features': [],
    }
    places = Places.objects.all()
    for place in places:
        place_slug = None
        if place.id == 2:
            place_slug = 'roofs24'
        elif place.id == 1:
            place_slug = 'moscow_legends'
        places_geo_json['features'].append({
              'type': 'Feature',
              'geometry': {
                'type': 'Point',
                'coordinates': [place.coordinate_lng, place.coordinate_lat]
              },
              'properties': {
                'title': place.title,
                'placeId': place_slug,
                'detailsUrl': f'https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/master/places/{place_slug}.json'
              }
        })
    context = {
        'places': places_geo_json,
    }

    return render(request, 'index.html', context=context)

def api_get_place(request, place_id):
    place = get_object_or_404(Places, pk=place_id)

    context = {
        'title': place.title,
        'imgs': [image.image.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.coordinate_lng,
            'lat': place.coordinate_lat,
        }

    }

    return JsonResponse(context)