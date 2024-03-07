from django.shortcuts import render,redirect
from .models import register_table ,product_tbl
from django.contrib import messages
from django.contrib.auth import login as authlogin,logout as authlogout,authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from cart.models import Direct_buy

# Create your views here.
def index(request):
    obj = product_tbl.objects.all()[:6]
    if obj:
        return render(request,'index.html',{"data":obj})
    else:
        return render(request,'index.html')
    

# def cart(request):
#     return render(request,'cart.html')

def contact(request):
    return render(request,'contact.html')

def productdetails(request):
 
    idn  = request.GET['idn']
    obj = product_tbl.objects.filter(id=idn)
   
    obj2 = Direct_buy.objects.all()
    obj2.delete()
    return render(request,"productdetails.html",{"data":obj})



def productpage(request):
    obj = product_tbl.objects.all()
    if obj:
        return render(request,'productpage.html',{"data":obj})
    else:
        return render(request,'productpage.html')






def register(request):
    if request.method=="POST":
        nam=request.POST.get('name')
        eml=request.POST.get('email')
        pas=request.POST.get('password')
  
        try:
            user = User.objects.create_user(first_name=nam,username=eml,password=pas)
            return redirect("/")
        except Exception as e:
            error = str(e)
        return render(request,"login.html")
    return render(request,"login.html")
    
def login(request):
    if request.method =="POST":
        em2=request.POST.get('email2')
        pass2=request.POST.get('password2')
        user = authenticate(username=em2,password=pass2)
        if user:
            authlogin(request,user)
            return redirect("/",{"user":user})
        else:
            messages.info(request,"Invalid email or password")
            return redirect("/login")
        
    return render(request,"login.html")   

def logout(request):
    authlogout(request)
    return redirect('/') 

def search(request):
    query = None

    if 'keyword' in request.GET:
        query = request.GET.get('keyword')
        products =product_tbl.objects.all().filter(Q(product_name__contains=query) | Q(product_price__contains=query))
        return render(request,'searchpage.html',{'query':query,'data':products})
    
def nike(request):
    obj =product_tbl.objects.filter(brand__iexact='nike')
    return render(request,"brandpage.html",{"data":obj})

def adidas(request):
    obj =product_tbl.objects.filter(brand__iexact='adidas')
    print(obj.query)
    return render(request,"brandpage.html",{"data":obj})
def fila(request):
    obj =product_tbl.objects.filter(brand__iexact='fila')
    return render(request,"brandpage.html",{"data":obj})
def bata(request):
    obj =product_tbl.objects.filter(brand__iexact='bata')
    return render(request,"brandpage.html",{"data":obj})
def newbalance(request):
    obj =product_tbl.objects.filter(brand__iexact='newbalance')
    return render(request,"brandpage.html",{"data":obj})
def vans(request):
    obj =product_tbl.objects.filter(brand__iexact='vans')
    return render(request,"brandpage.html",{"data":obj})
def puma(request):
    obj =product_tbl.objects.filter(brand__iexact='puma')
    return render(request,"brandpage.html",{"data":obj})
def converse(request):
    obj =product_tbl.objects.filter(brand__iexact='converse')
    return render(request,"brandpage.html",{"data":obj})