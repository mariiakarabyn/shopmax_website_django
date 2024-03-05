from django.shortcuts import render, get_object_or_404
from django.db.models import Count

from . models import Category, Product, Brand

def index(request):
    brands = Brand.objects.all()[3:9]        # Fetching first 6 logos
    categories = Category.objects.all()[:5]  # Fetching first 5 categories
    context = {
        'brands': brands,
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def regular(request):
    context= {}
    return render(request, 'regular-page.html', context)

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
