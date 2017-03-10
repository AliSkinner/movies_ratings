"""Module to handle external API calls and cleaning of data"""

import datetime
import requests
from movies_ratings.settings import THE_MOVIE_DB_KEY


BBC_URL = 'http://www.bbc.co.uk/tv/programmes/formats/films/player/episodes.json'
THE_MOVIE_DB_URL = 'http://api.themoviedb.org/3/search/movie?api_key={}'\
    .format(THE_MOVIE_DB_KEY)


def get_bbc_data():
    """Returns parsed list of data from BBC endpoint"""

    data = requests.get(BBC_URL).json()
    movies = [movie.get('programme') for movie in data.get('episodes')]
    return movies


def get_movie_db_data(movie):
    """
    Searches The Movie DB for title of given movie and returns dictionary
    of movie_details
    """

    search_data = requests.get(
        '{}&query={}'.format(
            THE_MOVIE_DB_URL,
            movie.get('title')
        )
    ).json()

    if search_data.get('total_results') > 0:
        movie_data = search_data.get('results')[0]
        movie['rating'] = movie_data.get('vote_average')

        if movie_data.get('release_date'):
            movie['release_date'] = datetime.datetime.strptime(
                movie_data.get('release_date'),
                '%Y-%m-%d'
            )

    return movie
