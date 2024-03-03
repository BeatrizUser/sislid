from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    fieldsets = (
        (None, {
            'fields': ('title','content','author')
        }),
        ('Imagem', {
            'fields': ('image', 'published_date')
        }),
    )
    search_fields = ['title', 'author', 'published_date'] 

admin.site.register(Post, PostAdmin)