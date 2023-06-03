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


class Images(models.Model):
    place = models.ForeignKey(
        Places,
        verbose_name='Место',
        related_name='images',
        on_delete=models.CASCADE,
    )
    image = models.ImageField(
        'Картинка',
    )
    weight = models.IntegerField(
        'Вес для сортировки',
        null=True,
        blank=True,
        default=1,
    )

    def __str__(self):
        return f'Фото №{self.id} для {self.place}'

    class Meta:
        verbose_name = 'фотография'
        verbose_name_plural = 'Фотографии'
