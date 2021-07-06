from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.RegisterPage,name="registerpage"),
    path("indexpage/",views.IndexPage,name="indexpage"),
    path('addbooks/',views.AddBooks,name="addbooks"),
    path("all-books/",views.ShowBookPage,name="showbook"),
    path("index-1/",views.NewPage,name="index1"),
    path("login-page/",views.LoginPage,name='loginpage'),
    path('logout/',views.logout,name="logout"),
    path("register/",views.RegisterUser,name="register"),
    path("login/",views.LoginUser,name="loginuser"),
]