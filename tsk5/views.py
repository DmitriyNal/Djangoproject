from django.shortcuts import render
from django.http import HttpResponse

from tsk5.forms import UserRegister

users = ['user1', 'user2', 'user3']


def sign_up_by_htm(request):
    info = {}  # Пустой словарь для передачи в context функции render

    if request.method == 'POST':
        login = request.POST.get('login')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        print(f'login: {login} ,password:{password} ,age:{age}')

        if password == repeat_password and age >= 18 and login not in users:
            return HttpResponse(f'"Приветствуем, {login}"')

    return render(request, 'fifth_tas/egistration_page.html', info)


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            print(f'login: {login} ,password:{password} ,age:{age}')
            if password == repeat_password and age >= 18 and login not in users:
                return HttpResponse(f'"Приветствуем, {login}"')
    else:
        form = UserRegister()
    info['form'] = form
    return render(request, 'fifth_tas/egistration_page.html', info)