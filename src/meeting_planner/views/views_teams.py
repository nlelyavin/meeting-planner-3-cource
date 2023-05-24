from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from meeting_planner.models import Team, Meeting


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
            }
        )
