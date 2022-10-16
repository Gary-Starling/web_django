
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('details', views.details, name='details'),
    path('debug',views.debug, name='debug')
]