import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from meeting_planner.constants import weekdays
from meeting_planner.forms import UserFreeTimeForm
from meeting_planner.models import Meeting, Team


class ProfileView(LoginRequiredMixin, View):
    """Класс описывающий профиль юзера"""

    def get(self, request, *args, **kwargs) -> HttpResponse:

        return render(
            request=request,
            template_name='meeting_planner/profile.html',
            context={
                'user': request.user,
                'free_time_form': UserFreeTimeForm
            },
        )


class MeetingsView(LoginRequiredMixin, View):
    """View для получения всех встреч пользователя за последнюю неделю"""

    def get(self, request):
        meetings = Meeting.objects.filter(
            team_id__in=Team.objects.filter(
                to_team__user_id=request.user.id,

            ),
            start_date_time__gt=self._get_nearest_monday()
        ).order_by('start_date_time', )

        return render(
            request=request,
            template_name='meeting_planner/meeting_schedule.html',
            context={
                'meetings': meetings,
                'weekdays': weekdays.values(),
            }
        )

    @staticmethod
    def _get_nearest_monday() -> datetime.date:
        """Возвращает ближайший понедельник на этой неделе с временем 0:00:00"""

        # Получение текущей даты
        current_date = datetime.date.today()

        # Определение разницы между текущим днем и понедельником (понедельник имеет индекс 0)
        days_ahead = (0 - current_date.weekday())

        # Вычисление ближайшего понедельника
        nearest_monday = current_date + datetime.timedelta(days=days_ahead)

        return nearest_monday

    @staticmethod
    def _get_nearest_weekday(weekday: int) -> datetime.date:
        """Возвращает ближайший день недели на этой неделе с временем 0:00:00"""

        # Получение текущей даты
        current_date = datetime.date.today()

        # Определение разницы между текущим днем и понедельником (понедельник имеет индекс 0)
        days_ahead = (weekday - current_date.weekday())

        # Вычисление ближайшего понедельника
        nearest_monday = current_date + datetime.timedelta(days=days_ahead)

        return nearest_monday
