from django.db.models import Count
from.models import Category


def header_categories(request):
    categories = Category.objects.annotate(
        product_count=Count('products')
    ).order_by('-product_count')[:10]
    return{
         'categories': categories
    }