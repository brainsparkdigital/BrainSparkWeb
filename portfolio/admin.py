# admin.py
from django.contrib import admin
from .models import Portfolio, PortfolioImage

class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("title", "short_detail", "details")  # Update the fields to display in the list view
    inlines = [PortfolioImageInline]  # Add the inline for PortfolioImage

admin.site.register(Portfolio, PortfolioAdmin)
