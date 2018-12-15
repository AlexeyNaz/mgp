from django import forms

from megagames.models import Ref


class LoginForm(forms.Form):
    name = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    widgets = {
        'password': forms.PasswordInput(),
    }


class PlayerForm(forms.Form):
    login = forms.CharField(label='Логин')
    firstName = forms.CharField(label='Имя')
    lastName = forms.CharField(label='Фамилия')
    sub = forms.ModelChoiceField(queryset=Ref.objects.filter(type='sub').values('name'), label='Подразделение')
    age = forms.IntegerField(label='Возраст')
    pid = forms.HiddenInput()
