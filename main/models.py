from django.db import models
from django.contrib.auth.models import User

class MovieModel(models.Model):
    movie_name = models.CharField(max_length=255)
    movie_genre = models.CharField(max_length=255)
    movie_year = models.CharField(max_length=255)   
    movie_cast = models.CharField(max_length=500) 
    movie_image = models.ImageField(upload_to='uploads', blank=True, max_length=500)
    site_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_name
