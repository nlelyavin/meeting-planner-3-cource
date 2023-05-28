from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from meeting_planner.models import CustomUser, UserFreeTime


class LoginForm(forms.Form):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль')


class UserFreeTimeForm(ModelForm):
    class Meta:
        model = UserFreeTime
        fields = ('start_datetime', 'end_datetime')


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            self.add_error('password1', 'Пароли не совпадают')
        return cleaned_data
