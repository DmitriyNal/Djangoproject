from django.contrib import admin
from django.urls import path
from tsk2.views import index, IndexView, home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', index, name='index'),
    path('credit/', IndexView.as_view()),
    path('', home_page, name='home')
]
