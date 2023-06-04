from django.shortcuts import render

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