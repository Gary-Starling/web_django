# Generated by Django 3.2.12 on 2022-10-16 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersinteam',
            name='who_add',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='user'),
            preserve_default=False,
        ),
    ]
