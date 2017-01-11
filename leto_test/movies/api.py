from django.core.cache import cache
import requests

BBC_URL = 'http://www.bbc.co.uk/tv/programmes/formats/films/player/episodes.json'

def get_bbc_data():
    movies = cache.get('movies', None)
    if movies:
        print 'movies from cache'
    else:
        print 'no movies in cache'
    if not movies:
        print 'getting movies'
        movies = requests.get(BBC_URL).json()
        cache.set('movies', movies, 5)
        print 'movies cached'
    return movies
