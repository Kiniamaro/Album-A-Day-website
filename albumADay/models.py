from django.db import models

# Create your models here.

class Genre(models.Model):
    genre_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.genre_name

class Album(models.Model):
    album_name = models.CharField(max_length=200)
    album_artist = models.CharField(max_length=500)
    album_year = models.IntegerField()
    ablum_comments = models.TextField()
    album_cover = models.CharField(max_length=500)
    genre = models.ManyToManyField(Genre)
    pub_date = models.DateTimeField('date published')
    
    def genre_names(self):
        return ', '.join([a.genre_name for a in self.genre.all()])
    genre_names.short_description = "Genres"
    
    def __str__(self):
        return self.album_name
