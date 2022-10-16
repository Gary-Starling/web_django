from dataclasses import field
from .models import UsersInTeam
from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput


class UserInTeamForm(ModelForm):
    class Meta:
        model = UsersInTeam
        fields = ['name', 'age', 'date_reg', 'who_add']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form',
                'placeholder': 'Name'
            }),

            "age": NumberInput(attrs={
                'class': 'form',
                'placeholder': 'Age'
            }),

            "date_reg": DateTimeInput(attrs={
                'class': 'form',
                'type': 'datetime-local',
                'placeholder': 'Date'
            }),

            "who_add": NumberInput(attrs={
                 'class': 'form',
                 'type': 'hidden',
                 'value': '1',  #Это заглушка для добавления в html от любого пользователя
                 'placeholder': 'id' #
            }),

        }
