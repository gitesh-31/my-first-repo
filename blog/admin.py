from django.contrib import admin
from .models import book

# Register your models here.

class bookadmin(admin.ModelAdmin):
    list_display=('title','author','published_date','pages')
    search_fields=('title','author')

admin.site.register(book, bookadmin)