from django.urls import path,include
from .import views

app_name='Zapatoapp'

urlpatterns = [
    path('',views.index),
    path('index',views.index,name='index'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    # path('cart',views.cart,name='cart'),
    path('contact',views.contact,name='contact'),
    path('productpage',views.productpage,name='productpage'),
    path('search/',views.search,name='search'),
    path('productdetails',views.productdetails,name='productdetails'),
    path('search/productdetails',views.productdetails,name='productdetails'),
    path('productdetails/<int:idn>/',views.productdetails,name='productdetails'),

    path('nike',views.nike,name='nike'),
    path('adidas',views.adidas,name='adidas'),
    path('fila',views.fila,name='fila'),
    path('newbalance',views.newbalance,name='newbalance'),
    path('vans',views.vans,name='vans'),
    path('puma',views.puma,name='puma'),
    path('bata',views.bata,name='bata'),
    path('converse',views.converse,name='converse'),
]