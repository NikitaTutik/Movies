import os
import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import MovieSearch
from .services import get_movie, get_top, get_movie_data
from .helpers import clean_top_data
from .models import MovieModel


def index(request):

    if request.method == 'GET':
        form = MovieSearch()

        if 'movie_name' in request.GET:
            form_data = get_movie(request.GET['movie_name'])
        else:
            form_data = None

        context = {'form': form, 'form_data': form_data}
        return render(request, 'main/index.html', context)

    elif request.method == 'POST':

        data = request.POST
        action = data.get("add")

        if action == "add":
            movie_data = get_movie(request.GET['movie_name'])

            MovieModel.objects.create(
             movie_name=movie_data['movie'][0], 
             movie_genre=movie_data['movie'][1],
             movie_year=movie_data['movie'][2],
             movie_cast=movie_data['movie'][3], 
             movie_image=movie_data['movie'][4], 
             site_user=request.user
            )
        return render(request, 'main/index.html')
    else:
        return render(request, 'main/index.html')

@login_required
def favorite_movies(request):

    obj = MovieModel.objects.filter(site_user_id=request.user.id)

    context = {'obj': obj}
    return render(request, 'main/favorite_movies.html', context)


def top_movies(request):

    movie_data = clean_top_data()
    context = {'movie_data': movie_data}
    return render(request, 'main/top.html', context)


