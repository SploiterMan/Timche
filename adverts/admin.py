from django.contrib import admin
from .models import Advert


class AdvertAdmin(admin.ModelAdmin):
    list_display = ["brand", "use", "gearbox", "phoneNumber", "color", "fuel"]
    list_filter = ['brand', 'use', 'gearbox', 'color', 'fuel', 'status']
    search_fields = ('slug', 'phoneNumber')



admin.site.register(Advert, AdvertAdmin)
