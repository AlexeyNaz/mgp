from django import forms

SUB_SHOICES = (
    ('Административная функция', 'Административная функция'),
    ('Безопасность', 'Безопасность'),
    ('Внутренний аудит', 'Внутренний аудит'),
    ('Закупки и логистика', 'Закупки и логистика'),
    ('Инфраструктура', 'Инфраструктура'),
    ('B2X', 'B2X'),
    ('B2G', 'B2G'),
    ('B2C', 'B2C'),
    ('PR', 'PR'),
    ('HR', 'HR'),
    ('Право', 'Право'),
    ('Финансы', 'Финансы'),
    ('Ритейл', 'Ритейл'),
    ('Кластер "Сохраняй"', 'Кластер "Сохраняй"'),
    ('ФедКК', 'ФедКК'),
    ('ФКК', 'ФКК'),
    ('TeleSale', 'TeleSale'),
    ('ФТМ', 'ФТМ'),
    ('Региональное отделение', 'Региональное отделение'),
    ('ПБК', 'ПБК'),
)


class LoginForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField()


class PlayerForm(forms.Form):
    login = forms.CharField()
    firstName = forms.CharField()
    lastName = forms.CharField()
    sub = forms.ChoiceField(choices=SUB_SHOICES)
    age = forms.IntegerField()
    pid = forms.HiddenInput()
