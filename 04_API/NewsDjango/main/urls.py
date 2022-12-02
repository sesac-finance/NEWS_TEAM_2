# Main URLConf(http://127.0.0.1:8000/main)
from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
]