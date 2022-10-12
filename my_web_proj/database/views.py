import re
from django.shortcuts import render, redirect
from .models import UsersInTeam
from .forms import UserInTeamForm   #, IdForm
from django.views.generic import DetailView
# Create your views here.

'''db start page and delete user from database '''


def db_start(requestuest):
    # Удаление пользователя из таблицы
    if requestuest.method == 'POST':
        Uid = requestuest.POST['user_id']            # Возьмём id удаляемого узера
        
        try:
            UserDelete = UsersInTeam.objects.get(id=Uid)
            UserDelete.delete()
            print("Record deleted successfully!")
        except:
            print("Record doesn't exists")

        users = UsersInTeam.objects.order_by('age')
        return render(requestuest, 'database/db.html', {'users': users})
    else:
        # Данные для вывода
        users = UsersInTeam.objects.order_by('age')
        # Передавать нужно по ключу
        return render(requestuest, 'database/db.html', {'users': users})


'''add new user into database '''


def add(request):

    errors = ''

    # Добавление нового пользователя в таблицу БД
    if request.method == 'POST':
        UserAdd = UserInTeamForm(request.POST)
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

    # Передавать нужно по ключу
    return render(request, 'database/add.html', data)


'''dynamic page database/1 database/2'''


class NewUserView(DetailView):
    model = UsersInTeam
    template_name = 'database/user_detail.html'
    context_object_name = 'user_key'
