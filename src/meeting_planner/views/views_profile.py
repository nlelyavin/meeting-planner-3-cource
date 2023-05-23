from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class ProfileView(LoginRequiredMixin, View):
    """Класс описывающий профиль юзера"""

    def get(self, request, *args, **kwargs) -> HttpResponse:
        return render(request=request, template_name='meeting_planner/profile.html', context={'user': request.user})
