from django.urls import path
from . import views

app_name = 'coopmain'       # 네임스페이스 이름

urlpatterns = [
    path('', views.index, name='index'),    # name - url 별칭
]