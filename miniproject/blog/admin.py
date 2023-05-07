from django.contrib import admin
from .models import Articale


class ArticalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')

admin.site.register (Articale, ArticalAdmin)
