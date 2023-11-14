from django.contrib import admin
from .models import Film

# Register your models here.
# class FilmAdmin(admin.ModelAdmin):
#     list = ('naziv', 'zanr', 'uloge')

admin.site.register(Film)
