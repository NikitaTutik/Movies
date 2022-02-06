import os
from django.shortcuts import render
from .forms import MovieSearch
from .services import get_movie

def index(request):
    if request.method == 'GET':
        form = MovieSearch(request.GET)

        if 'movie_name' in request.GET:
            form_data = get_movie(request.GET['movie_name'])
        else:
            form_data = None

        context = {'form': form, 'form_data': form_data}
        return render(request, 'main/index.html', context)
    else:
        return render(request, 'main/index.html')

