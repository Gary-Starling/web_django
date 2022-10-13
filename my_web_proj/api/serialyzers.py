from rest_framework import serializers  # json
from database.models import UsersInTeam # для модели представленияы


class UserSerialyzer(serializers.ModelSerializer):
    class Meta:
        model = UsersInTeam  # Модель представления данных будет нашего типа из datbase
        fields = ['id', 'name', 'age', 'date_reg']
