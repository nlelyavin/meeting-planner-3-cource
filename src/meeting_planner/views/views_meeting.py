from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from meeting_planner.models import Meeting


class MeetingView(LoginRequiredMixin, View):

    def get(self, request, pk):
        meeting = Meeting.objects.get(id=pk)

        return render(
            request,
            template_name='meeting_planner/meeting.html',
            context={
                'meeting': meeting,
            }
        )
