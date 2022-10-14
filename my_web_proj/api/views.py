
from . serialyzers import UserSerialyzer
from rest_framework import generics

from database.models import UsersInTeam
from rest_framework.views import APIView
from rest_framework.response import Response

from api import serialyzers


''' Представления для DRF '''


'''Получить всех пользователей'''
# URL <base>/api/v1/users/
class UsersInfoView(generics.ListAPIView):
    queryset = UsersInTeam.objects.all()
    serializer_class = UserSerialyzer
    '''
    def get(self, request):
        all_users = UsersInTeam.objects.all()
        serialyzer = UserSerialyzer(all_users, many=True)
        return Response({'all_users' : serialyzer.data})
    '''


'''Получить всех пользователй отсортированных  по id'''
# URL <base>/api/v1/users/sortedByAge
class UsersInfoViewSorted(generics.ListAPIView):
    queryset = UsersInTeam.objects.order_by('age')
    serializer_class = UserSerialyzer


'''Тоже самое по вохрасту'''
# URL <base>/api/v1/users/sortedById
class UsersInfoViewSorted(generics.ListAPIView):
    queryset = UsersInTeam.objects.order_by('id')
    serializer_class = UserSerialyzer


'''Получить данные о пользователе по url'''
# URL <base>/api/v1/users/<userId>
class UserInfoView(generics.RetrieveAPIView):  # single model instance.
    queryset = UsersInTeam.objects.all()
    serializer_class = UserSerialyzer


'''С использованием serializers'''
# URL <base>/v1/get/all/
# URL <base>/v1/post/AddNew/
class UserAPIView(APIView):

    ''' Получить все записи из бд'''
    #get
    def get(self, request):
        lst = UsersInTeam.objects.all().values()  # Получим значения из БД
        all = UserSerialyzer(lst, many=True)      # Приведём к виду для json ответа [OrderDict]
        # Выведем весь список пользователей в бд
        return Response({'Users': all.data})

    ''' Добавить запись в бд'''

    ''' Форма данных для отправки в формате JSON
    "Users": [
    {
        "id": 1,
        "name": "Name",
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
    #post
    def post(self, request):
        
        serializer = UserSerialyzer(data=request.data) #Запрос к форме
        serializer.is_valid(raise_exception=True)      #Проверка правильносьт ввода
        serializer.save()                              #выовет create в serializers/py
        
        '''
        new_user = UsersInTeam.objects.create(
            name=request.data['name'],          #Выберем все поля из JSON запроса
            age=request.data['age'],
            date_reg=request.data['date_reg'],
        )
        '''

        #При правильном вводе отправим обратно
        return Response({'AddUser': serializer.data})
    #put
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error":"not allowed"})
        try:
            instance = UsersInTeam.objects.get(pk=pk)
        except:
            return Response({"error":"id doesn't exist"})
        
        #OK запись и ключ существуют
        serializer = UserSerialyzer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'Put': serializer.data})
    
    #
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error":"not allowd"})
        try:
            instance = UsersInTeam.objects.get(pk=pk)
        except:
            return Response({"error":"id doesn't exist"})

        #OK
        instance.delete()
        return Response({'Delete': 'delete user with id = ' + str(pk)})
