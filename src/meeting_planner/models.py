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


class TeamToUser(models.Model):
    user = ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Пользователь',
                      related_name='to_user')
    team = ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Команда',
                      related_name='to_team')


class Meeting(models.Model):
    name = CharField(max_length=50, verbose_name='Название Встречи')

    team = ForeignKey(Team, on_delete=models.CASCADE, related_name='meeting_to_team', verbose_name='Команда', )

    start_date_time = models.DateTimeField(verbose_name='Начало встречи', null=True, blank=True)
    end_date_time = models.DateTimeField(verbose_name='Конец встречи', null=True, blank=True)
    day = models.CharField(max_length=15, verbose_name='День недели', null=True, blank=True)

    def get_start_time(self) -> str:
        return self.start_date_time.strftime('%H:%m')

    def get_end_time(self) -> str:
        return self.end_date_time.strftime('%H:%m')


class UserFreeTime(models.Model):
    """Свободное время пользователя. Для составления встреч в свободное время"""
    user = ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')

    start_datetime = models.DateTimeField(verbose_name='Начало свободного времени', null=True, blank=True)
    end_datetime = models.DateTimeField(verbose_name='Конец свободного времени', null=True, blank=True)