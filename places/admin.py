from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Places, Images


class ImagesInline(admin.TabularInline):
    model = Images
    readonly_fields = ['preview_image']
    extra = 1

    def preview_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="200">')


@admin.register(Places)
class PlacesAdmin(admin.ModelAdmin):
    inlines = (ImagesInline,)


admin.site.register(Images)