from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced


# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        grocery = Product.objects.filter(category='G')
        fruits = Product.objects.filter(category='Fr')
        vegetables = Product.objects.filter(category='V')
        fashion = Product.objects.filter(category='Fa')
        home_applinces = Product.objects.filter(category='H')
        electronics = Product.objects.filter(category='E')
        kids = Product.objects.filter(category='K')
        return render(request, 'app/home.html', {'grocery' : grocery, 'fruits' : fruits, 'vegetables' : vegetables, 'fashion' : fashion, 'home_applinces' : home_applinces, 'electronics' : electronics, 'kids' : kids})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product' : product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
