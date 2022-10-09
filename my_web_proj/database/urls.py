from django.urls import path
from . import views

urlpatterns = [
    path('', views.db_start, name='db_start'),
]