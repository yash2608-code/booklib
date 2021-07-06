from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def IndexPage(request):
    return render(request, "app/index.html")

def ShowBookPage(request):
    if 'id' in request.session and 'email' in request.session:
        AllbookData = Book.objects.all()
        print(f"--------------------->ALL BOOK DATA->{AllbookData}")
        return render(request, "app/showbooks.html",{'data':AllbookData})
    else:
        return redirect('loginpage')

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
            request.session['id'] = user[0].id
            request.session['fname'] = user[0].fname
            request.session['email'] = user[0].email
            return redirect("showbook")
        else:
            msg = "Password is incorrect"
            return render(request, "app/login.html",{'err':msg})
    else:
        msg = "Seller Doesn't Found"
        return render(request, "app/login.html",{'err':msg})

def logout(request):
    del request.session['id']
    del request.session['fname']    
    del request.session['email']
    return redirect('loginpage')

def AddBooks(request):
    bname = request.POST['Bname']
    aname = request.POST['Aname']
    cat = request.POST['Bcate']
    bimg = request.FILES['Bimg']
    book = request.FILES['Book']
    bprice = float(request.POST['Bookp'])

    category = Category.objects.create(Cname=cat)
    book = Book.objects.create(
        Book_name=bname,
        Author_name=aname,
        Book_category=category,
        Book_img = bimg,
        Book = book,
        BookPrice = bprice
    )
    return redirect("showbook")