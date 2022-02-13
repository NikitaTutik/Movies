import requests
import os


headers = {
    'x-rapidapi-host': "imdb8.p.rapidapi.com",
    'x-rapidapi-key': os.environ.get('IMDB_KEY')
    }


def get_movie(name):
        movie_list = []
        url = "https://imdb8.p.rapidapi.com/auto-complete"

        querystring = {"q": name}


        response = requests.request("GET", url, headers=headers, params=querystring)

        APIdata = response.json()

        movie_name = APIdata['d'][0]['l']
        movie_genre = APIdata['d'][0]['q']
        movie_year = APIdata['d'][0]['y']
        movie_cast = APIdata['d'][0]['s']
        movie_image = APIdata['d'][0]['i']['imageUrl']
        movie_list.extend((movie_name, movie_genre, movie_year, movie_cast, movie_image))

        movie_data = {"movie": movie_list}

        return movie_data


def get_top():
    url = "https://imdb8.p.rapidapi.com/title/get-top-rated-tv-shows"

    response = requests.request("GET", url, headers=headers)

    data = response.json()

    return data


def get_movie_data(movie):

    url = "https://imdb8.p.rapidapi.com/title/get-details"

    querystring = {"tconst": movie}

    response = requests.request("GET", url, headers=headers, params=querystring)    

    data = response.json()

    return data
