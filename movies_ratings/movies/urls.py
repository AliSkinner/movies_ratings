from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^', views.MovieList.as_view(), name='movies')
]
