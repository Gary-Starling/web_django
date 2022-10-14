from django.urls import path
from .views import UsersInfoView, UserInfoView, UserAPIView, UsersInfoViewSorted

#CRUD
#create+
#read+
#update
#delete

urlpatterns = [
    path('v1/users/', UsersInfoView.as_view()),
    path('v1/users/<int:pk>/', UserInfoView.as_view()),
    path('v1/users/sortedByAge', UsersInfoViewSorted.as_view()),
    path('v1/users/sortedById', UsersInfoViewSorted.as_view()),
    path('v1/get/all/', UserAPIView.as_view()),
    path('v1/post/AddNew/', UserAPIView.as_view()),
]