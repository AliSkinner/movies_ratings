"""module to house constructor function for movie object"""
import time
import datetime
import logging

logger = logging.getLogger(__name__)


def custom_movie_object(movie):
    """constructs dictionary of movie data"""

    movie_details = {
        'title': movie.get('title'),
        'synopsis': movie.get('short_synopsis'),
        'run_time': time.strftime('%H:%M:%S', time.gmtime(movie.get('duration'))),
        'expire_string': movie.get('media').get('availability'),
        'poster': 'http://ichef.bbci.co.uk/images/ic/480x270/{}.jpg'
                  .format(movie.get('image').get('pid')),
        'rating': 'Not Rated',
        'release_date': 'Unkown'
    }

    try:
        movie_details['available_until'] = datetime.datetime.strptime(
            movie.get('available_until')[:10],
            '%Y-%m-%d'
        )
    except Exception as e:
        logger.debug(e)

    try:
        movie_details['available_from'] = datetime.datetime.strptime(
            movie.get('actual_start')[:10],
            '%Y-%m-%d'
        )
    except Exception as e:
        logger.debug(e)

    return movie_details
