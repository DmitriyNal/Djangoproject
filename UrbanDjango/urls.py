from django.contrib import admin
from django.urls import path
from tsk2.views import index, IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index/', IndexView.as_view())
]
