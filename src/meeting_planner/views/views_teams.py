from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from meeting_planner.models import Team, CustomUser


class TeamsView(LoginRequiredMixin, View):

    def get(self, request):

        teams = Team.objects.filter(to_team__user_id=request.user.id)

        return render(request, 'meeting_planner/teams.html', {'teams': teams})

    # def post(self, request):
    #     self.form = RegistrationForm(request.POST)
    #
    #     if self.form.is_valid():
    #         user = self.form.save()
    #         login(request, user)
    #         return redirect('main')
    #
    #     return render(request, 'meeting_planner/registration.html', {
    #         'form': self.form
    #     })
    #
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return redirect('main')
    #
    #     return super().dispatch(request, *args, **kwargs)
