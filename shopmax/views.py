from django.shortcuts import render
from django.db.models import Count

from . models import Category

def index(request):
    context= {}
    return render(request, 'index.html', context=context)

def regular(request):
    context= {}
    return render(request, 'regular-page.html', context)

def shop(request):
    context= {}
    return render(request, 'shop.html', context)

def single_blog(request):
    context= {}
    return render(request, 'single-blog.html', context)

def single_product_details(request):
    context= {}
    return render(request, 'single-product-details.html', context)

def blog(request):
    context= {}
    return render(request, 'blog.html', context)

def checkout(request):
    context= {}
    return render(request, 'checkout.html', context)

def contact(request):
    context= {}
    return render(request, 'contact.html', context)
