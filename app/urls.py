from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login,name='login'),
    path('register/add2/login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('login/add/',views.add,name='add'),
    path('register/add2/login/add/',views.registerToLogin,name='registerToLogin'),
    path('register/add2/',views.add2,name='add2'),
]

