import re
from django.shortcuts import render
from .models import UsersInTeam


# Create your views here.


'''db start page'''
def db_start(req):
    users = UsersInTeam.objects.order_by('age')
    return render(req,'database/db.html', {'users':users}) #Передавать нужно по ключу