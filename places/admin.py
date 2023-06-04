from django.contrib import admin

# Register your models here.
from .models import Places, Images


class ImagesInline(admin.TabularInline):
    model = Images
    extra = 1

@admin.register(Places)
class MasterAdmin(admin.ModelAdmin):
    inlines = (ImagesInline,)


admin.site.register(Images)