from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return render(request, 'func_templates.html')


class IndexView(TemplateView):
    template_name = 'class-templates.html'
