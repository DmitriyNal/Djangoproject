from django import forms


class UserRegister(forms.Form):
    login = forms.CharField(label='Логин', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput, min_length=8)
    repeat_password = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput, min_length=8)
    age = forms.IntegerField(label='Возраст', max_value=120)
