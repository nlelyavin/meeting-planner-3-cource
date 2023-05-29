import datetime
from typing import List

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.views import View

from meeting_planner.constants import weekdays
from meeting_planner.forms import MeetingForm
from meeting_planner.models import Team, Meeting, CustomUser, UserFreeTime


class TeamsView(LoginRequiredMixin, View):

    def get(self, request):
        teams = Team.objects.filter(to_team__user_id=request.user.id)

        return render(request, 'meeting_planner/teams.html', {'teams': teams})


class TeamView(LoginRequiredMixin, View):

    def get(self, request, pk):
        team = Team.objects.get(id=pk)
        meetings = Meeting.objects.filter(team_id=pk)

        return render(
            request,
            'meeting_planner/team.html',
            context={
                'team': team,
                'meetings': meetings,
                'create_form': MeetingForm,
            }
        )

    def post(self, request, pk):
        meeting_form = MeetingForm(request.POST)

        if meeting_form.is_valid():
            team = Team.objects.get(id=pk)
            users_team = CustomUser.objects.filter(to_user__team=team)

            free_time_users = UserFreeTime.objects.filter(user__in=users_team)
            free_times_intersections = self.find_longest_non_overlapping_intersections(users_free_time=free_time_users)

            self.create_meetings(free_times_intersections, team, meeting_form)

        return redirect('main')

    @staticmethod
    def create_meetings(free_times_intersections, team, meeting_form):
        for free_time in free_times_intersections:
            free_time: List[datetime.datetime] = free_time
            if not isinstance(free_time, UserFreeTime):
                Meeting(
                    team=team,
                    start_date_time=free_time[0],
                    end_date_time=free_time[1],
                    day=weekdays[free_time[0].date().weekday()],
                    name=meeting_form.cleaned_data['name'],
                ).save()

    def find_longest_non_overlapping_intersections(self, users_free_time):
        """
        Находит самые длинные непересекающиеся пересечения в списке отрезков времени.

        Аргументы:
        - segments: список отрезков времени, представленных в формате (start, end), где start и end - объекты типа datetime.

        Возвращает:
        Список самых длинных непересекающихся пересечений в исходном списке.

        Примечания:
        - Пересечение включает границы отрезков.
        """
        users_free_time: List[UserFreeTime] = users_free_time

        sorted_segments = sorted(users_free_time, key=lambda x: x.start_datetime)
        non_overlapping_intersections = []

        for segment in sorted_segments:
            if not self.is_overlapping_with_list(segment, non_overlapping_intersections):
                non_overlapping_intersections.append(segment)
            else:
                self.replace_overlapping_intersection(segment, non_overlapping_intersections)

        return non_overlapping_intersections

    def is_overlapping_with_list(self, segment, intersection_list):
        """
        Проверяет, пересекается ли отрезок с любым отрезком из списка.

        Аргументы:
        - segment: отрезок времени, представленный в формате (start, end).
        - intersection_list: список отрезков времени.

        Возвращает:
        True, если отрезок пересекается с любым отрезком из списка, иначе False.
        """

        for inter in intersection_list:
            if self.is_overlapping(segment, inter):
                return True
        return False

    def replace_overlapping_intersection(self, segment, intersection_list):
        """
        Заменяет пересекающееся пересечение на новое пересечение, если оно длиннее.

        Аргументы:
        - segment: отрезок времени, представленный в формате (start, end).
        - intersection_list: список отрезков времени.

        Примечания:
        - Функция изменяет переданный список intersection_list.
        """

        longest_duration = datetime.timedelta(0)
        longest_intersection = None

        for i, inter in enumerate(intersection_list):
            start, end = self.get_intersection(segment, inter)
            if not start:
                continue

            duration = end - start

            if duration > longest_duration:
                longest_duration = duration
                longest_intersection = [start, end]

                intersection_list.remove(intersection_list[i])
                intersection_list.append(longest_intersection)

    @staticmethod
    def is_overlapping(segment1, segment2):
        """
        Проверяет, пересекаются ли два отрезка времени.

        Аргументы:
        - segment1: первый отрезок времени, представленный в формате (start, end).
        - segment2: второй отрезок времени, представленный в формате (start, end).

        Возвращает:
        True, если отрезки пересекаются, иначе False.
        """

        return segment1.start_datetime < segment2.end_datetime and segment2.start_datetime < segment1.end_datetime

    @staticmethod
    def get_intersection(segment1, segment2):
        """
        Возвращает пересечение двух отрезков времени.

        Аргументы:
        - segment1: первый отрезок времени, представленный в формате (start, end).
        - segment2: второй отрезок времени, представленный в формате (start, end).

        Возвращает:
        Отрезок времени, представленный в формате (start, end), обозначающий пересечение двух отрезков.
        Если пересечения нет, возвращает None.
        """

        start = max(segment1.start_datetime, segment2.start_datetime)
        end = min(segment1.end_datetime, segment2.end_datetime)

        if start < end:
            segment1.delete()
            segment2.delete()
            return start, end
        else:
            return None, None
