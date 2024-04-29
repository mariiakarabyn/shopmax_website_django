from django.db.models import Count, Avg
from .models import Category

def header_categories(request):
    top_categories = Category.objects.annotate(
        product_count=Count('products')
    ).order_by('-product_count')[:15]
    
    best_price = Category.objects.annotate(
        avg_price=Avg('products__price')
    ).order_by('avg_price')[:6]
    
    return {
        'categories': top_categories,
        'best_price': best_price
    }
    
