from django.urls import path
from .views import index, favorite_movies, top_movies


urlpatterns = [
    path('', index, name = 'index'),
    path('favorites/', favorite_movies, name='favorite'),
    path('top/', top_movies, name='top')
]