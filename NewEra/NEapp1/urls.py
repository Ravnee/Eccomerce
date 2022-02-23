
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home, name='home'),
    path('google/',views.google,name='google'),
    path('OurProducts/',views.OurProducts, name='OurProducts'),
    path('ContactUs/',views.cont,name='ContactUs'),
    path('episodes/',views.episodes,name='episodes'),
    path('card/',views.card,name='card'),         
    path('modalregister/',views.modalregister,name='modalregister'),
    path('modalsignin/',views.modalsignin,name = "modalsignin"),
    path('userlogin/',views.clientdash,name = "userlogin"),
    path('adminlogin/',views.admindash,name = "adminlogin"),
    path('logout',views.logouts,name='logout'),
    path('cart/', views.cart,name='cart'),
    path("checkout",views.checkout, name="checkout"),  
    path("order",views.Orders, name="order"),
    ]
