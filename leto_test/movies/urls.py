from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^', views.MovieList.as_view(), name="movies")
]
