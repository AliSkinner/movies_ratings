from django.contrib import messages
from django.views.generic import TemplateView

from movies.api import get_bbc_data

class MovieList(TemplateView):

    template_name = 'movies.html'

    def get_context_data(self, **kwargs):
        context = super(MovieList, self).get_context_data(**kwargs)
        try:
            movies = get_bbc_data()
            context['movies'] = movies.get('episodes')
        except:
            messages.error(self.request, 'Error getting data from BBC')
        return context
