from django.contrib import admin
from .models import *


class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cat', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'cat')


admin.site.register(Women, WomenAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    ordering = ('id',)

admin.site.register(Category, CategoryAdmin)
 