import os
from django.shortcuts import render
from .forms import MovieSearch
import requests

def index(request):
    if request.method == 'GET':
        form = MovieSearch(request.GET)

        url = "https://imdb8.p.rapidapi.com/auto-complete"

        querystring = {"q":"game of thr"}

        headers = {
            'x-rapidapi-host': "imdb8.p.rapidapi.com",
            'x-rapidapi-key': os.environ.get('IMDB_KEY')
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        APIdata = response.json()

        print(APIdata) #temp test
        context = {'form': form}
        return render(request, 'main/index.html', context)
    else:
        return render(request, 'main/index.html')

