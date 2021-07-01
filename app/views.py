from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def IndexPage(request):
    return render(request, "app/index.html")

def RegisterPage(request):
    return render(request, "app/register.html")

def LoginPage(request):
    return render(request, "app/login.html")

def NewPage(request):
    return render(request, "app/index-1.html")

def RegisterUser(request):
    if request.method == 'POST':
        fn = request.POST['fname']
        ln = request.POST['lname']
        em = request.POST['email']
        pwd = request.POST['passwd']

        slr = Seller.objects.create(fname=fn,lname=ln,email=em,passwd=pwd)

        return redirect("loginpage")
    else:
        msg = "Method Changes"
        return render(request,"app/register.html",{'err':msg})
    
def LoginUser(request):
    em = request.POST['email']
    pwd = request.POST['passwd']

    user = Seller.objects.filter(email=em)

    if len(user) > 0:
        if user[0].passwd == pwd:
            return redirect("indexpage")
        else:
            msg = "Password is incorrect"
            return render(request, "app/login.html",{'err':msg})
    else:
        msg = "Seller Doesn't Found"
        return render(request, "app/login.html",{'err':msg})