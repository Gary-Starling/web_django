from django.shortcuts import render

from rest_framework import generics
from .import serialyzers
from database.models import UsersInTeam

# Create your views here.
'''get'''
class UsersList(generics.ListAPIView):
    queryset = UsersInTeam.objects.all()
    serializer_class = serialyzers.UserSerialyzer