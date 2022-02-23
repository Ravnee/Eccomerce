from optparse import Values
from unicodedata import category
# from os import uname
from django import http
from django.http import request
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from importlib_metadata import email
from sklearn.naive_bayes import CategoricalNB
from sympy import re
from urllib3 import Retry
from .models import admin_login, contact_info, order,product,Category
from django.contrib.auth.hashers import make_password,check_password

# print(make_password('Naman@123'))
# print(check_password('Naman@123','pbkdf2_sha256$320000$O50ortkMb2K3FXPDquQ871$PDAKTgpu9oToBVkRk2hlVL3xLo8/YHCZUv3kWFTEsMo='))
def home(request):
    return render(request,'home.html')

def google(request):
    return render(request,'google.html')

def OurProducts(request):
    
    if request.method == "POST":
        product_id = request.POST.get('cartid')
        remove = request.POST.get('minus') 
        cart_id = request.session.get('cart')

        if cart_id:
            quantity = cart_id.get(product_id)
            if quantity:
                if remove:
                    if quantity <=1:
                        cart_id.pop(product_id)
                    else:
                        cart_id[product_id] = quantity -1
                else:
                    cart_id[product_id] = quantity +1
            else:
                cart_id[product_id]  = 1
        else:
            cart_id ={}
            cart_id[product_id] = 1
        
        request.session['cart'] =cart_id
        print(request.session['cart'])


    cate  = Category.objects.all()
    fil_by_cat = request.GET.get('category')
    if fil_by_cat:
        pro = product.objects.filter(category_id= fil_by_cat)
    else:
        pro = product.objects.all()
    context = {
        'pro':pro,
        'cat':cate
    }
    return render(request,'OurProducts.html',context)

def cont(request):
    return render(request,'ContactUs.html')

# def reg(request):
#     if request.method == 'POST':
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         email = request.POST.get('email')
#         gender = request.POST.get('gender')
#         print(fname,lname,email,gender)
#         contact = contact_info(firstname=fname,lastname=lname, email=email,gender = gender)
#         contact.save()
#         return HttpResponseRedirect('../')
#     return render(request,'register.html')

def episodes(request):
    return render(request,'episodes.html')

def card(request):
    return render(request,'card.html')       
   
def modalregister(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        new_password = request.POST.get('newpass')
        print(fname,lname,email,gender,new_password)
        contact = contact_info(firstname=fname,lastname=lname, email=email,gender = gender, user_password = make_password(new_password))
        contact.save()
        return HttpResponseRedirect('../')
    return render(request,'register.html')

def modalsignin(request):
    error_msg = None

    if request.method == "POST":
        email = request.POST.get('email')
        print(email)
        password = request.POST.get("newpass")
        print(password)
        try:
            fetch_email = contact_info.objects.get(email=email)
            print(fetch_email)
            if(fetch_email.email == email):
                print("--------------")
                flag = check_password(password,fetch_email.user_password)
                print(flag)
                if flag:
                    print("-----------------",flag)
                    request.session['email'] = fetch_email.email
                    request.session['customer_id'] = fetch_email.id
                    print(request.session['email'])
                    request.session['firstname'] = fetch_email.firstname 
                    return redirect('home')
                else:
                    error_msg = "Please Enter valid password"
                    return render(request,'home.html',{'error_msg':error_msg})
        except:
            error_msg = "Please enter valid email"
            return render(request,'home.html',{'error_msg': error_msg})
        return HttpResponse(fetch_email.email, fetch_email.password)

    # if request.method=='POST':
    #     first_name = request.POST.get("fname")
    #     pass_word = request.POST.get("newpass")

    #     print(first_name,pass_word)
    #     user_login = contact_info.objects.filter(firstname=first_name, user_password = pass_word)

    #     if user_login:
    #         request.session['username'] = first_name
    #         print(request.session['username'])
            
    #         return redirect('home')
        
    #     a_login = admin_login.objects.filter(admin_username=first_name)

    #     if a_login:
    #         request.session['username'] = first_name
    #         request.session['customer_id'] = email.id
    #         print(request.session['username'])

    #         return HttpResponseRedirect('../adminlogin')
    # return render(request,'home.html')

def clientdash(request):
    # c = request.session['username']
    return render(request,'clientdash.html')

def admindash(request):
    c = request.session['username']
    return render(request,'admindash.html',{'c':c})

def logouts(request):
    print('ghhhhhhhh--------')
    request.session.clear()
   
    return redirect('home')

def cart(request):

    ids = list(request.session.get('cart').keys())
    cart_pro = product.objects.filter(id__in = ids)
    print(cart_pro)
    return render(request,'cart.html',{'cart_pro':cart_pro})

def checkout(request):
    if request.method == 'POST':
        address = request.POST.get("address")
        print(address)
        mobile = request.POST.get("mobile")
        print(mobile)
        customer_id = request.session.get("customer_id")
        cart = request.session.get('cart')
        products = product.objects.filter(id__in=list(cart.keys()))

        for pro in products:
            save_order_dtls=order(
                customer=contact_info(id=customer_id),
                product = pro,
                price = pro.price,
                quantity = cart.get(str(pro.id)),
                address = address,
                phone = mobile,)
            save_order_dtls.save() 
    print(address,mobile,cart,products)  
    request.session['cart']={}          
    return redirect('cart')

def Orders(request):
    customer= request.session.get('customer_id')
    ord_dtls = order.objects.filter(customer=customer).order_by('-date')
    tp = 0
    for i in ord_dtls:
        tp += (i.price * i.quantity) 
    return render(request,'order.html',{'ord_dtl': ord_dtls,'tp':tp})


# #user session
# def user_login(request):
#     if request.method=='POST':
#             username = request.POST['fname']
#             S = contact_info.objects.filter(name ='fname').values('fname')
#             if S:
#                 request.session['un'] = S


# #admin session
# def admin_login(request):
#     if request.method=='POST':
#             username = request.POST['fname']
#             S = User.objects.filter(name ='fname').values('fname')
#             if S:
#                 request.session['an'] = S

# def admin_dash(request):
#     c = request.session['fn']
#     User.objects.filter(fname = c).values('lname')

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('email')
#         password = request.POST.get('passw')
#         print(email,passw)
#         contact = contact_info(username=email,Password=passw)
#         contact.save()
#         return HttpResponseRedirect('../')
#     # return render(request,'register.html')





    






