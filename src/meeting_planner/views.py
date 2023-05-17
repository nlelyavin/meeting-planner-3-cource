from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from meeting_planner.forms import LoginForm


def index(request):
    return render(request=request, template_name='meeting_planner/profile.html')


class LoginView(View):
    form = LoginForm

    def get(self, request, *args, **kwargs):
        return render(request, 'meeting_planner/signIn.html', {'form': self.form})

    def post(self, request, *args, **kwargs):
        self.form = LoginForm(request.POST)

        if self.form.is_valid():
            username = self.form.cleaned_data['username']
            password = self.form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                self.form.add_error('username', 'Неправильный логин или пароль')
            else:
                login(request, user)
                return redirect('main')

        return render(request, 'meeting_planner/signIn.html', {'form': self.form})

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')

        return super().dispatch(request, *args, **kwargs)


def registration(request):
    return render(request=request, template_name='meeting_planner/registration.html')


class ProfileView(LoginRequiredMixin, View):
    """Класс описывающий профиль юзера"""

    def get(self, request, *args, **kwargs) -> HttpResponse:
        return render(request=request, template_name='meeting_planner/profile.html', context={'user': request.user})
