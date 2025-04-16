from django.shortcuts import render, redirect
from .models import *

from django.http import HttpResponse
def addproducts(request):
    return render(request,'addproducts.html')
def projecthome(request):
    return render(request,'projecthome.html')
def sellerhome(request):
    return render(request,'sellerhome.html')
def home(request):
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')
def thank_you(request):
    return render(request,'thank_you.html')

def feedback(request):
    return render(request,'feedback.html')

# Correct import statement


from .models import Feedback

def feedback1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')

        feedback = Feedback.objects.create(name=name, email=email, rating=rating, comment=comment)
        feedback.save()

        return render(request, 'thank_you.html')

    return render(request, 'feedback.html')

def thank_you(request):
    return render(request, 'thank_you.html')
def login1(request):
    if request.method == 'POST':
        username=request.POST['username']
        pass1=request.POST['password']
        user = auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request, user)
            if len(username)==10:
                return redirect('home')
            elif len(username)==4:
                return redirect('sellerhome')
            else:
                return redirect('sellerhome')
        else:
            messages.info(request,'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request,'home.html')
def logout(request):
    auth.logout(request)
    return render(request, 'home.html')


def signup(request):
    return render(request,'signup.html')

from django.contrib import messages
from django.contrib.auth.models import User,auth
def signup1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, '00PS! Username already taken.')
                return render(request, 'signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'home.html')
        else:
            messages.info(request, 'Password doesnot match.')
            return render(request, 'signup.html')





def lounge(request):
    return render(request,'lounge.html')
def office(request):
    return render(request,'office.html')
def wooden(request):
    return render(request,'wooden.html')
def lhs(request):
    return render(request,'lhs.html')
def sofa3(request):
    return render(request,'sofa3.html')
def sofa2(request):
    return render(request,'sofa2.html')
def serveware(request):
    return render(request,'serveware.html')
def diningtables(request):
    return render(request,'diningtables.html')
def knives(request):
    return render(request,'knives.html')
def study(request):
    return render(request,'study.html')
def officetable(request):
    return render(request,'officetable.html')
def computertable(request):
    return render(request,'computertable.html')
def door2(request):
    return render(request,'door2.html')
def door3(request):
    return render(request,'door3.html')
def door4(request):
    return render(request,'door4.html')
def lamp(request):
    return render(request,'lamp.html')
def ceiling(request):
    return render(request,'ceiling.html')
def outdoor(request):
    return render(request,'outdoor.html')
def single(request):
    return render(request,'single.html')
def double(request):
    return render(request,'double.html')
def bunk(request):
    return render(request,'bunk.html')
def lounge9(request):
    return render(request,'lounge9.html')
def cart(request):
    context={}
    return render(request,'cart.html',context)
def buynow(request):
    return render(request,'buynow.html')

def pay(request):
    return render(request,'pay.html')

def view_seller_products(request):
    if request.method == 'GET':
        product_details_list = ProductDetails.objects.all()
        return render(request, 'viewmyproducts.html', {'product_details_list': product_details_list})
def newproducts(request):
    if request.method == 'GET':
        product_details_list = ProductDetails.objects.all()
        return render(request, 'newproducts.html', {'product_details_list': product_details_list})
def credit(request):
    return render(request,'credit.html')





def add_details(request):
    if request.method=='POST':
        name = request.POST.get('productname')
        price = request.POST.get('price')
        category = request.POST.get('productcatg')
        description = request.POST.get('productdesc')
        picture = request.FILES.get('picture')

        product_details=ProductDetails(
            name=name,
            price=price,
            category=category,
            description=description,
            picture=picture,
        )
        product_details.save()
        return render(request,'datainserted.html')
    return render(request,'sellerhome.html')



'''
# views.py
from django.shortcuts import render, redirect
from .models import Cart
from myapp.models import Product

def add_to_cart(request, product_id):
    product = Product.objects.get(pk=product_id)
    user = request.user

    # Check if the item is already in the cart, update the quantity
    cart_item, created = Cart.objects.get_or_create(user=user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')  # Redirect to the cart page


'''