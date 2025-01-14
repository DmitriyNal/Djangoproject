from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    title = 'Главная страница'
    auto = 'Автомобили в наличии'
    offers = 'Специальные предложения'
    context = {'title': title, 'auto': auto, 'offers': offers}

    return render(request, "second_tsk/main.html", context)


def home_page(request):
    title = 'Главная страница'
    shop = 'Магазин'
    credit = 'Кредит'
    choise = 'Выберите раздел'
    context = {'title': title, 'shop': shop, 'credit': credit, 'choise': choise}

    return render(request, "second_tsk/Base.html", context)


class IndexView(TemplateView):
    template_name = 'second_tsk/kredit.html'
