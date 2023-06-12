from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from .models import Place

def index(request):
    places_geo = {
        'type': 'FeatureCollection',
        'features': [],
    }
    for place in Place.objects.all():
        place_geo = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.coordinate_lng, place.coordinate_lat]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('get_place', kwargs={'place_id':place.id}),
            }
        }
        places_geo['features'].append(place_geo)

    context = {
        'places': places_geo,
    }

    return render(request, 'index.html', context=context)

def api_get_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
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
    return JsonResponse(context, json_dumps_params={
        'ensure_ascii': False,
        'indent': 2,
    })