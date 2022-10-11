import re
from django.shortcuts import render, redirect
from .models import UsersInTeam
from .forms import UserInTeamForm, IdForm
from django.views.generic import DetailView
# Create your views here.

'''db start page and delete user from database '''


def db_start(request):

    #Данные для вывода
    users = UsersInTeam.objects.order_by('age')

    # Удаление пользователя из таблицы
    if request.method == 'POST':
        test = request.POST.getlist('test')
        dtest = { 'dtest' : test }
        return render(request, 'database/test.html',dtest)

    # Передавать нужно по ключу  CRUD django
    return render(request, 'database/db.html', {'users': users} )


'''add new user into database '''

def add(req):

    errors = ''

    # Добавление нового пользователя в таблицу БД
    if req.method == 'POST':
        UserAdd = UserInTeamForm(req.POST)
        if UserAdd.is_valid():
            UserAdd.save()
            return redirect('home')
        else:
            errors = 'Wrong input data'

    users = UserInTeamForm()

    # Форма для выввода
    data = {
        'users': users,
        'errors': errors
    }

    return render(req, 'database/add.html', data)  # Передавать нужно по ключу


'''dynamic page database/1 database/2'''

class NewUserView(DetailView):
    model = UsersInTeam
    template_name = 'database/user_detail.html'
    context_object_name = 'user_key'