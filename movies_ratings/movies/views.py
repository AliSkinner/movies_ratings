import logging
from django.contrib import messages
from django.core.cache import cache
from django.views.generic import TemplateView
from movies.api import get_bbc_data, get_movie_db_data
from movies.lib.object.movie import custom_movie_object
from movies.lib.sorting.sort import sort_movies


# Get an instance of a logger
logger = logging.getLogger(__name__)


class MovieList(TemplateView):
    """Movies listing page"""

    template_name = 'movies.html'

    def get_context_data(self, **kwargs):
        context = super(MovieList, self).get_context_data(**kwargs)

        # check cache for movies
        movies = cache.get('movies', None)
        sort_by = self.request.GET.get('sort_by', 'recent')

        if not movies:
            try:
                # get data from BBC API
                bbc_movies = get_bbc_data()
            except Exception as e:
                messages.error(
                    self.request,
                    'Error getting data from BBC'
                )
                logger.debug(e)
                return context
            movies = [custom_movie_object(movie) for movie in bbc_movies]
            try:
                # search The Movie DB for each movie
                movies = [get_movie_db_data(movie) for movie in movies]
                # save results to cache for 5 minutes
                cache.set('movies', movies, 300)
            except Exception as e:
                messages.error(
                    self.request,
                    'Error getting data from The Movie DB'
                )
                logger.debug(e)
                return context

        movies = sort_movies(movies, sort_by)
        context['movies'] = movies

        return context
