from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableStackedInline, SortableAdminBase

from .models import Place, Image


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['preview_image']
    extra = 1

    def preview_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="200">')


@admin.register(Place)
class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = (ImageInline,)
    search_fields = ['title']

admin.site.register(Image)