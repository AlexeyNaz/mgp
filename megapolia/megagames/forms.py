from django import forms

from megagames.models import Ref


class LoginForm(forms.Form):
    name = forms.CharField(label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')
    widgets = {
        'password': forms.PasswordInput(),
    }


class RefChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class PlayerForm(forms.Form):
    login = forms.CharField(label='Логин')
    firstName = forms.CharField(label='Имя')
    lastName = forms.CharField(label='Фамилия')
    sub = RefChoiceField(queryset=Ref.objects.filter(type='sub'), label='Подразделение')
    age = forms.IntegerField(label='Возраст')
    pid = forms.HiddenInput()
