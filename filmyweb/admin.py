from django.contrib import admin
from .models import Film

#admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    #fields = ["tytul", "opis", "rok"]
    #exclude = ["opis"]
    list_display = ["tytul",'rok','imdb_rating']
    list_filter = ["film_genre"]
    search_fields = ["tytul","opis"]