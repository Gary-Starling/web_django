from tabnanny import verbose
from django.db import models

# Create your models here.

class UsersInTeam(models.Model): #Наследуем от models.Model
    name = models.CharField('Username', max_length = 100)
    age = models.IntegerField('Age')
    date_reg = models.DateTimeField('Date restration')

    def __str__(self):
        return self.name
