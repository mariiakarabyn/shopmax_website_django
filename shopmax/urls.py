from django.urls import path
from .views import index, regular, catalog, single_blog, single_product_details, blog, checkout, contact

urlpatterns = [
    path('', index, name='index' ),
    path('regular/', regular, name='regular' ),
    path('catalog/', catalog, name='catalog' ),
    path('single_blog/', single_blog, name='single_blog' ),
    path('single_product_details/', single_product_details, name='single_product_details' ),
    path('blog/', blog, name='blog' ),
    path('checkout/', checkout, name='checkout' ),
    path('contact/', contact, name='contact' ),
    
]