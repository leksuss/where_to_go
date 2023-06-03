from django.db import models

# Create your models here.

class Places(models.Model):
    title = models.CharField(
        'Название места',
        max_length=100,
    )
    description_short = models.CharField(
        'Краткое описание',
        max_length=255,
        null=True,
        blank=True,
    )
    description_long = models.TextField(
        'Длинное описание',
        null=True,
        blank=True,
    )
    coordinate_lat = models.FloatField(
        'Широта',
    )
    coordinate_lng = models.FloatField(
        'Долгота',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'место'
        verbose_name_plural = 'Места'
