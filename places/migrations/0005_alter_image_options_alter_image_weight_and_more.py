# Generated by Django 4.2.2 on 2023-06-12 10:44

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20230612_1036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['weight'], 'verbose_name': 'фотография', 'verbose_name_plural': 'Фотографии'},
        ),
        migrations.AlterField(
            model_name='image',
            name='weight',
            field=models.PositiveIntegerField(blank=True, db_index=True, default=0, null=True, verbose_name='Вес для сортировки'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, default='', verbose_name='Длинное описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, default='', verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название места'),
        ),
    ]
