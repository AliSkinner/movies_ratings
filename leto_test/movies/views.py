from django.contrib import messages
from django.core.cache import cache
import logging
from movies.api import get_bbc_data, get_movie_details
from django.views.generic import TemplateView
from django.http import HttpResponse

# Get an instance of a logger
logger = logging.getLogger(__name__)

class MovieList(TemplateView):
    """Movies listing page"""

    template_name = 'movies.html'

    def get_context_data(self, **kwargs):
        context = super(MovieList, self).get_context_data(**kwargs)

        # check cache for movies
        movies = cache.get('movies', None)

        if not movies:
            try:
                # get data from BBC API
                bbc_movies = get_bbc_data()
            except:
                messages.error(
                    self.request,
                    'Error getting data from BBC'
                )
                return context
            try:
                # search The Movie DB for each movie
                movies = [get_movie_details(movie) for movie in bbc_movies]
                # save results to cache for 5 minutes
                cache.set('movies', movies, 300)
            except:
                messages.error(
                    self.request,
                    'Error getting data from The Movie DB'
                )
                return context

        context['movies'] = movies

        return context
