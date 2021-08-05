from django.contrib import admin
from .models import Books, Characters


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'authors', 'publisher', 'released')

@admin.register(Characters)
class CharactersAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'culture', 'aliases')