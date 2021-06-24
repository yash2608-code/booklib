from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.RegisterPage,name="registerpage"),
    path("indexpage/",views.IndexPage,name="indexpage"),
    path("login-page/",views.LoginPage,name='loginpage'),
    path("register/",views.RegisterUser,name="register"),
    path("login/",views.LoginUser,name="loginuser"),
]