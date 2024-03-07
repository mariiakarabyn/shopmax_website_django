from typing import Any
from django.shortcuts import render, get_object_or_404
from django.db.models import Count

from . models import Category, Product, Brand

from django.views.generic import TemplateView, ListView, DetailView

class RegularViev(TemplateView):
    template_name = 'regular-page.html'


def index(request, slug=None):
    if slug is not None:
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(categories=category)[:9]
    else:
        products = Product.objects.all()[:5]

    brands = Brand.objects.all()[3:9]
    context = {
        'brands': brands,
        'products': products
    }
    return render(request, 'index.html', context=context)



def shop(request, **kwargs):
    category = get_object_or_404(Category, slug=kwargs.get('slug'))
    products = Product.objects.filter(categories=category)[:9]
    context= {
        'products': products
    }
    return render(request, 'shop.html', context)

def single_blog(request):
    context= {}
    return render(request, 'single-blog.html', context)

def product(request, **kwargs):
    single_product = get_object_or_404(Product, slug=kwargs.get('slug'))
    context= {
        'product': single_product
    }
    return render(request, 'product.html', context)

def blog(request):
    context= {}
    return render(request, 'blog.html', context)

def checkout(request):
    context= {}
    return render(request, 'checkout.html', context)

def contact(request):
    context= {}
    return render(request, 'contact.html', context)
