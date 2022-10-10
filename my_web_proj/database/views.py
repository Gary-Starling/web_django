import re
from django.shortcuts import render,redirect
from .models import UsersInTeam
from .forms import UserInTeamForm
from django.views.generic import DetailView
# Create your views here.

'''db start page'''
def db_start(req):
    users = UsersInTeam.objects.order_by('age')
    return render(req,'database/db.html', {'users':users}) #Передавать нужно по ключу



'''add new user'''
def add(req):

    errors = ''

    #Добавление нового пользователя в таблицу БД
    if req.method == 'POST':
        UserAdd = UserInTeamForm(req.POST)
        if UserAdd.is_valid():
            UserAdd.save()
            return redirect('home')
        else:
            errors = 'Wrong input data'

    users = UserInTeamForm()

    #Форма для выввода
    data = {
        'users' : users,
        'errors': errors
    }

    return render(req,'database/add.html', data) #Передавать нужно по ключу



class NewUserView(DetailView):
    model = UsersInTeam
    template_name = 'database/user_detail.html'
    context_object_name = 'user_key'

