from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, "main.html")


def home_page(request):
    return render(request, "Base.html")


class IndexView(TemplateView):
    template_name = 'kredit.html'
