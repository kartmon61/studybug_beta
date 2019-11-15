from django.urls import path
from .import views

urlpatterns = [
    #메인 페이지
    path('',views.main,name='main'),  
]