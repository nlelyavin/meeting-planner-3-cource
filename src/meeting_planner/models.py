from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, ForeignKey


class CustomUser(AbstractUser):
    pass


class Team(models.Model):
    name = CharField(max_length=50, verbose_name='Название команды')
    password = CharField(max_length=128, verbose_name='Пароль команды')

    team_creator = ForeignKey(
        CustomUser, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Создатель команды',
        related_name='team_creator_to_user'
    )

    def __init__(self, *args, **kwargs):
        init = super().__init__(*args, **kwargs)


class TeamToUser(models.Model):
    user = ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Пользователь',
                      related_name='to_user')
    team = ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Команда',
                      related_name='to_team')


class Meeting(models.Model):
    name = CharField(max_length=50, verbose_name='Название Встречи')

    team = ForeignKey(Team, on_delete=models.CASCADE, related_name='meeting_to_team', verbose_name='Команда', )


class UserFreeTime(models.Model):
    """Свободное время пользователя. Для составления встреч в свободное время"""

    start_time = models.DateTimeField(verbose_name='Начало свободного времени')
    end_time = models.DateTimeField(verbose_name='Конец свободного времени')
