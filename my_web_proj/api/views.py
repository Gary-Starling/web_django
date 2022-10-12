from django.shortcuts import render

from rest_framework import generics
from .import serialyzers
from database.models import UsersInTeam

# Create your views here.
'''get all users'''
class UsersList(generics.ListAPIView):
    queryset = UsersInTeam.objects.all()
    serializer_class = serialyzers.UserSerialyzer

'''get 1 user'''
class UserInfo(generics.RetrieveAPIView):
    queryset = UsersInTeam.objects.all()
    serializer_class = serialyzers.UserSerialyzer

