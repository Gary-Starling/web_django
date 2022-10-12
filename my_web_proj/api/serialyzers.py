from pyexpat import model
from rest_framework import serializers #json
#from django.contrib.auth.models import User
from database.models import UsersInTeam

class UserSerialyzer(serializers.ModelSerializer):
    class Meta:
        model = UsersInTeam
        fields = ['id', 'name', 'age', 'date_reg']
