from django.contrib import admin
from albumADay.models import Album, Genre
# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('album_name', 'album_artist', 'album_year', 'genre_names', 'pub_date')
    search_fields = ['album_name']
    filter_horizontal = ('genre',)
    
    
admin.site.register(Album, AlbumAdmin)
admin.site.register(Genre)
