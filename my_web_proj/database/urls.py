from django.urls import path
from . import views

urlpatterns = [
    path('', views.db_start, name='db_start'),
    path('add', views.add, name='add'),
    path('<int:pk>', views.NewUserView.as_view(), name='users')
]