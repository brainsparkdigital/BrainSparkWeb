from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'created_at')
    readonly_fields = ('slug',)  # Include this if you want to display the slug in the admin

    # If you have specified fieldsets or fields, do not include 'slug' if it is not editable

admin.site.register(Post, PostAdmin)
