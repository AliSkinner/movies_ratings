from django.core.cache import cache
import requests

BBC_URL = 'http://www.bbc.co.uk/tv/programmes/formats/films/player/episodes.json'

def get_bbc_data():
    # check cache for movies
    movies = cache.get('movies', None)
    if not movies:
        data = requests.get(BBC_URL).json()
        movies = [movie.get('programme') for movie in data.get('episodes')]
        # cache movies for 5 mins
        cache.set('movies', movies, 300)
    return movies
