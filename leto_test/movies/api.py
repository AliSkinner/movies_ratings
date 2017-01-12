"""Module to handle external API calls and cleaning of data"""

import datetime
import logging
import requests
import time

from leto_test.settings import THE_MOVIE_DB_KEY

logger = logging.getLogger(__name__)

BBC_URL = "http://www.bbc.co.uk/tv/programmes/formats/films/player/episodes.json"
THE_MOVIE_DB_URL = "http://api.themoviedb.org/3/search/movie?api_key={}"\
    .format(THE_MOVIE_DB_KEY)

def get_bbc_data():
    """Returns parsed list of data from BBC endpoint"""

    data = requests.get(BBC_URL).json()
    movies = [movie.get('programme') for movie in data.get('episodes')]
    return movies

def get_movie_details(movie):
    """Searches The Movie DB for title of given movie and returns dictionary
        of movie_details
    """

    # make dictionary of required data
    movie_details = {
        'title': movie.get('title'),
        'synopsis': movie.get('short_synopsis'),
        'run_time': time.strftime("%H:%M:%S", time.gmtime(movie.get('duration'))),
        'expires': movie.get('media').get('availability'),
        'poster': "http://ichef.bbci.co.uk/images/ic/480x270/{}.jpg"
                  .format(movie.get('image').get('pid')),
        'rating': 'Not Rated',
        'release_date': "Unkown"
    }

    search_data = requests.get("{}&query={}"
        .format(
            THE_MOVIE_DB_URL,
            movie.get('title')
        )
    ).json()

    if search_data.get('total_results') > 0:
        movie_data = search_data.get('results')[0]
        movie_details['rating'] = movie_data.get('vote_average')
        try:
            movie_details['release_date'] = datetime.datetime.strptime(
                movie_data.get('release_date'),
                '%Y-%m-%d'
            )
        except Exception as e:
            logger.debug(e)
            pass

    return movie_details
