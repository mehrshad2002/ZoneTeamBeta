from django.contrib import admin
from .models import Hubmodel

class HubAdmin(admin.ModelAdmin):
    pass

admin.site.register(Hubmodel , HubAdmin)
