from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UsersInTeam(models.Model):  # Наследуем от models.Model
    
    name = models.CharField('Username', max_length=100)
    age = models.IntegerField('Age')
    date_reg = models.DateTimeField('Date')
    #Наследуемся отсюда from django.contrib.auth.models import User(Все пользователи)/при удалении пользователя, удаляются все его записи
    who_add = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE) #id того кто добавил

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

