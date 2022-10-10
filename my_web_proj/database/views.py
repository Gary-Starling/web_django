import re
from django.shortcuts import render
from .models import UsersInTeam
from .forms import UserInTeamForm

# Create your views here.


'''db start page'''
def db_start(req):
    users = UsersInTeam.objects.order_by('age')
    return render(req,'database/db.html', {'users':users}) #Передавать нужно по ключу


'''add new user'''
def add(req):

    users = UserInTeamForm()

    data = {
        'users' : users
    }

    return render(req,'database/add.html', data) #Передавать нужно по ключу