from django.contrib import admin
from django.urls import path
# from tsk2.views import index, IndexView, home_page
from tsk4.views import index, IndexView, home_page
from tsk5.views import sign_up_by_htm, sign_up_by_django

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', index, name='index'),
    path('credit/', IndexView.as_view()),
    path('', home_page, name='home'),
    path('registration/', sign_up_by_htm),
    path('registration2/', sign_up_by_django)

]
