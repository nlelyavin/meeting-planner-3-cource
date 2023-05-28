from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View

from meeting_planner.forms import LoginForm, RegistrationForm


def index(request):
    return render(request=request, template_name='meeting_planner/index.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('main')


class RegistrationView(View):
    form = RegistrationForm

    def get(self, request):
        return render(request, 'meeting_planner/registration.html', {
            'form': self.form
        })

    def post(self, request):
        self.form = RegistrationForm(request.POST)

        if self.form.is_valid():
            user = self.form.save()
            login(request, user)
            return redirect('main')

        return render(request, 'meeting_planner/registration.html', {
            'form': self.form
        })

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')

        return super().dispatch(request, *args, **kwargs)


class LoginView(View):
    form = LoginForm

    def get(self, request):
        return render(request, 'meeting_planner/login.html', {'form': self.form})

    def post(self, request):
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

        return render(request, 'meeting_planner/login.html', {'form': self.form})

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('main')

        return super().dispatch(request, *args, **kwargs)
