from django.urls import path
from .views import UsersInfoView, UserInfoView, UserAPIView, UsersInfoViewSorted

#CRUD
#create+
'''
POSTMAN
query
    POST:127.0.0.1:8000/api/v1/post/AddNew/
    body : {
    "name": "Myname",
    "age": 17,
    "date_reg": "2022-08-05T8:30:10Z"
    }

response
    {
    "AddUser": {
        "id": 31,
        "name": "Myname",
        "age": 17,
        "date_reg": "2022-08-05T08:30:10Z"
    }
}
json
'''
#create+

#read+
'''
POSTMAN
query
    GET:127.0.0.1:8000/api/v1/get/all
    body:no
response
json
{
    "Users": [
        {
            "id": 1,
            "name": "Igor",
            "age": 29,
            "date_reg": "2022-11-07T08:29:10Z"
        },
        {
            "id": 2,
            "name": "Gary",
            "age": 25,
            "date_reg": "2022-10-09T11:30:00Z"
        },
        {..........
'''
#read+


#update+
'''
query
    PUT:127.0.0.1:8000/api/v1/post/update/<id-user>/
    body : {
    "name": "new",                      //change name
    "age": 17,                          //change age
    "date_reg": "2022-08-05T8:30:10Z"   //change date
    }

response
    {
    "Put": {
        "id": 32,
        "name": "HideMePls",
        "age": 30,
        "date_reg": "2022-11-07T08:30:10Z"
    }
    }
}
json
'''

#delete

urlpatterns = [
    path('v1/users/', UsersInfoView.as_view()),                     #Показать все(get)
    path('v1/users/<int:pk>/', UserInfoView.as_view()),             #Показать конкретный по id(get)
    path('v1/users/sortedByAge', UsersInfoViewSorted.as_view()),    #Показать отсортированный по возрасту(get)
    path('v1/users/sortedById', UsersInfoViewSorted.as_view()),     #Показать отсортированный по id(get)
    path('v1/get/all/', UserAPIView.as_view()),                     #Показать все, но через APIView
    path('v1/post/AddNew/', UserAPIView.as_view()),                 #Добавить нового юзера(post/create)
    path('v1/post/update/<int:pk>/', UserAPIView.as_view())         #Изменить данные юзера(put/update)
]