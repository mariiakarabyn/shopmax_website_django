from django.shortcuts import render

from . models import Category

def index(request):
    categories = Category.objects.all()[:10]
    context= {
        'categories': categories
    }
    return render(request, 'index.html', context=context)

def regular(request):
    return render(request, 'regular-page.html')

def shop(request):
    return render(request, 'shop.html')

def single_blog(request):
    return render(request, 'single-blog.html')

def single_product_details(request):
    return render(request, 'single-product-details.html')

def blog(request):
    return render(request, 'blog.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')
