#from dataclasses import field
from .models import UsersInTeam
from django.forms import ModelForm, TextInput, DateTimeInput, NumberInput


class UserInTeamForm(ModelForm):
    class Meta:
        model = UsersInTeam
        fields = ['name', 'age', 'date_reg']

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
            })
        }
