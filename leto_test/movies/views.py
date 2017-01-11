from django.views.generic import TemplateView

class MovieList(TemplateView):
    template_name = 'movies.html'

    def get_context_data(self, **kwargs):
        context = super(MovieList, self).get_context_data(**kwargs)
        context['test'] = 'hi'
        return context
