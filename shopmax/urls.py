from django.urls import path
from .views import index, RegularViev, shop, single_blog, product, blog, checkout, contact

urlpatterns = [
    path('', index, name='index' ),
    path('regular/', RegularViev.as_view(), name='regular' ),
    path('shop/<slug:slug>/', shop, name='shop' ),
    path('single_blog/', single_blog, name='single_blog' ),
    path('product/<slug:slug>/', product, name='product' ),
    path('blog/', blog, name='blog' ),
    path('checkout/', checkout, name='checkout' ),
    path('contact/', contact, name='contact' ),
    
]