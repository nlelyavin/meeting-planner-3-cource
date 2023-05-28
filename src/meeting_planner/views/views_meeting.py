import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from meeting_planner.constants import weekdays
from meeting_planner.models import Meeting


class MeetingView(LoginRequiredMixin, View):

    def get(self, request, pk):
        meeting = Meeting.objects.get(id=pk)

        # monday_nearest = self._get_nearest_monday()

        time_line = {
            'start': meeting.get_start_time(),
            'end': meeting.get_end_time(),
            'weekday': meeting.day,
        }

        return render(
            request,
            template_name='meeting_planner/meeting.html',
            context={
                'meeting': meeting,
                'weekdays': weekdays,
                'time_line': time_line,
            }
        )



