from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    readonly_fields = ['preview_image']
    extra = 1

    def preview_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="200">')


@admin.register(Place)
class PlacesAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)


admin.site.register(Image)