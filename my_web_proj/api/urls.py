from django.urls import include
from django.urls import path, re_path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
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
json
    {
    "Put": {
        "id": 32,
        "name": "HideMePls",
        "age": 30,
        "date_reg": "2022-11-07T08:30:10Z"
    }
    }
}

'''

#delete
'''
query
    DELETE:127.0.0.1:8000/api/v1/post/Delete/<id>/
    body : no
response
json
{
    "Delet": "delete user with id = 2"
}

'''

'''
urlpatterns = [
    path('v1/users/', UsersInfoView.as_view()),                     #Показать все(get)
    path('v1/users/<int:pk>/', UserInfoView.as_view()),             #Показать конкретный по id(get)
    path('v1/users/sortedByAge', UsersInfoViewSorted.as_view()),    #Показать отсортированный по возрасту(get)
    path('v1/users/sortedById', UsersInfoViewSorted.as_view()),     #Показать отсортированный по id(get)
    path('v1/get/all/', UserAPIView.as_view()),                     #Показать все, но через APIView
    path('v1/post/AddNew/', UserAPIView.as_view()),                 #Добавить нового юзера(post/create)
    path('v1/post/Delete/<int:pk>/', UserAPIView.as_view())         #Удалить юзера(delete)
]
'''

urlpatterns = [
    path('v1/auth/', include('djoser.urls')),                                       #djoser
    re_path(r'v1/auth/', include('djoser.urls.authtoken')),                         # 
    path('v1/users/', ApiUsersInfoView.as_view()),                                  #Показать все(get)
    path('v1/users/<int:pk>/', ApiUserInfoView.as_view()),                          #Показать конкретный по id(get)
    path('v1/users/sortedByAge/', ApiUsersInfoViewSortedAge.as_view()),             #Показать отсортированный по возрасту(get)
    path('v1/users/sortedById/', ApiUsersInfoViewSortedId.as_view()),               #Показать отсортированный по id(get)
    path('v1/post/AddNew/', ApiUserAdd.as_view()),                                  #Добавить нового юзера(post/create)
    path('v1/put/ChangeUser/<int:pk>/', ApiUserUpdate.as_view()),                   #Изменить данные юзера(put)
    path('v1/delete/<int:pk>/', ApiUserDelete.as_view()),                           #Удалить юзера(delete)
    #path('v1/update_with_token/<int:pk>/',ApiUserUpdateToken.as_view())            #Обновить данные юзера с помощью токена(djoser)
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),     #jwt
    path('v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    #
    path('v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),       #
    path('v1/jwt/GetPUT/<int:pk>/', ApiUserJwtInfoView.as_view()),       #
]