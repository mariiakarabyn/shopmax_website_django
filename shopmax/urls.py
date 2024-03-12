from django.urls import path
from .views import index, RegularViev, shop, SigdleBlogViev, product, BlogViev, CheckoutViev, ContactViev, AllProductsViev

urlpatterns = [
    path('', index, name='index' ),
    path('regular/', RegularViev.as_view(), name='regular' ),
    path('blog/', BlogViev.as_view(), name='blog' ),
    path('single_blog/', SigdleBlogViev.as_view(), name='single_blog' ),
    path('checkout/', CheckoutViev.as_view(), name='checkout' ),
    path('contact/', ContactViev.as_view(), name='contact' ),
    path('shop/<slug:slug>/', shop, name='shop' ),
    path('product/', AllProductsViev.as_view(), name='all_products' ),
    path('product/<slug:slug>/', product, name='product' ),
    
    
]