from operator import concat
from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome),
    path('author', views.author),
    #path('')
]