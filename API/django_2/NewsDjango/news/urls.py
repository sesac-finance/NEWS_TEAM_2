from django.urls import path
from . import views

urlpatterns = [
    path('newsDomain/', views.getTbDomain, name="newsDomain"),
    path('newsDomain_one/<str:name>',views.getTbDomain_one,name="newsDomainOne")
]

# 추천 된거를 디비에서 가지고 온다. 
# dump 