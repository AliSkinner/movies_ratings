from django.contrib import messages
from django.core.cache import cache
from django.views.generic import TemplateView

from movies.api import get_bbc_data, get_movie_details

class MovieList(TemplateView):

    template_name = 'movies.html'

    def get_context_data(self, **kwargs):
        context = super(MovieList, self).get_context_data(**kwargs)
        movies = cache.get('movies', None)
        if not movies:
            try:
                bbc_movies = get_bbc_data()
            except:
                messages.error(self.request, 'Error getting data from BBC')
                return context
            try:
                movies = [get_movie_details(movie) for movie in bbc_movies]
                cache.set('movies', movies, 300)
            except:
                messages.error(self.request, 'Error getting data from The Movie DB')
                return context
        context['movies'] = movies
        return context
