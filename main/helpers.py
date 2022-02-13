from .services import get_top, get_movie_data

def clean_top_data():

    top_movies = get_top()
    movie_cleaned_data = []
    movie_data = {}

    for i in top_movies:
        for key, value in i.items():
            if key == 'id':
                movie_cleaned_data.append(value[7:-1])
    count = 0
    for j in movie_cleaned_data:
        if count != 16:
            count += 1
            movie_data.update({count: get_movie_data(j)})
    
    return movie_data 

    
