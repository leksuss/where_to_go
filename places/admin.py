from django.contrib import admin

# Register your models here.
from .models import Places, Images

admin.site.register(Places)
admin.site.register(Images)