from django.contrib import admin
from django.utils.html import format_html

from adminsortable2.admin import SortableStackedInline, SortableAdminBase

from .models import Place, Image


class ImageInline(SortableStackedInline):
    model = Image
    readonly_fields = ['preview_image']
    extra = 1

    def preview_image(self, image):
        return format_html('<img src="{}" height="200">', image.image.url)


@admin.register(Place)
class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = (ImageInline,)
    search_fields = ['title']


admin.site.register(Image)
