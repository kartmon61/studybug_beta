from django.urls import path, include
from .import views

urlpatterns = [
    #메인 페이지
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('accounts/',include('allauth.urls')),
    path('',views.loading,name='loading'),
    path('signup2/',views.signup2,name='signup2'),
]