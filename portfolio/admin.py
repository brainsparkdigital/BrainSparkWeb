from django.contrib import admin

from .models import PortFolio

class PortFolioAdmin(admin.ModelAdmin):
    list_display = ("title", "body",)

admin.site.register(PortFolio, PortFolioAdmin)