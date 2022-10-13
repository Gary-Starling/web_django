
from . serialyzers import UserSerialyzer
from rest_framework import generics

from database.models import UsersInTeam
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict


''' Представления для DRF '''

# Create your views here.

'''get all users'''
# api/v1/users/


class UsersInfoView(generics.ListAPIView):
    queryset = UsersInTeam.objects.all()
    serializer_class = UserSerialyzer
    '''
    def get(self, request):
        all_users = UsersInTeam.objects.all()
        serialyzer = UserSerialyzer(all_users, many=True)
        return Response({'all_users' : serialyzer.data})
    '''


'''get all users sorted by age'''
# api/v1/users/sortedByAge


class UsersInfoViewSorted(generics.ListAPIView):
    queryset = UsersInTeam.objects.order_by('age')
    serializer_class = UserSerialyzer


'''get all users sorted by age'''
# api/v1/users/sortedById


class UsersInfoViewSorted(generics.ListAPIView):
    queryset = UsersInTeam.objects.order_by('id')
    serializer_class = UserSerialyzer


'''get 1 user'''
# api/v1/users/<userId>


class UserInfoView(generics.RetrieveAPIView):  # single model instance.
    queryset = UsersInTeam.objects.all()
    serializer_class = UserSerialyzer


''''''


class UserAPIView(APIView):
    ''' Получить все записи из бд'''

    def get(self, request):
        lst = UsersInTeam.objects.all().values()  # Получим значения из БД
        # Выведем весь список пользователей в бд
        return Response({'Users': lst})

    ''' Отправить запись в бд'''

    ''' Форма данных для отправки в формате JSON
    "Users": [
    {
        "id": 1,
        "name": "igor",
        "age": 29,
        "date_reg": "2022-10-10T11:29:10Z"
    },
    {
        "id": 2,
        "name": "Gary",
        "age": 25,
        "date_reg": "2022-10-09T11:30:00Z"
    },
    '''

    def post(self, request):
        #тут нужен try
        new_user = UsersInTeam.objects.create(
            name=request.data['name'],          #Выберем все поля из JSON запроса
            age=request.data['age'],
            date_reg=request.data['date_reg'],
        )
        #При правильном вводе отправим обратно
        return Response({'AddUser': model_to_dict(new_user)})
