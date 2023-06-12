from urllib.parse import urlparse
from pathlib import Path
import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Load place data to DB'

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            help='url to json file with place data',
        )

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()

        place = response.json()
        place_obj, is_created = Place.objects.get_or_create(
            title=place['title'],
            coordinate_lat=place['coordinates']['lat'],
            coordinate_lng=place['coordinates']['lng'],
            defaults={
                'description_short': place['description_short'],
                'description_long': place['description_long'],
            }
        )
        if is_created:
            for image_url in place['imgs']:
                self.load_place_images(image_url, place_obj)

    def load_place_images(self, image_url, place_obj):
        response = requests.get(image_url)
        response.raise_for_status()

        image = Image.objects.create(place=place_obj)

        filename = Path(urlparse(image_url).path).name
        image.image.save(filename, ContentFile(response.content), save=True)
