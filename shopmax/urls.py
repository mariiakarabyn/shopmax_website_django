from django.urls import path
from .views import IndexView, RegularViev, ShopView, SigdleBlogViev, ProductView, BlogViev, CheckoutViev, ContactViev, AllProductsViev

urlpatterns = [
    path('', IndexView.as_view(), name='index' ),
    path('regular/', RegularViev.as_view(), name='regular' ),
    path('blog/', BlogViev.as_view(), name='blog' ),
    path('single_blog/', SigdleBlogViev.as_view(), name='single_blog' ),
    path('checkout/', CheckoutViev.as_view(), name='checkout' ),
    path('contact/', ContactViev.as_view(), name='contact' ),
    path('shop/<slug:slug>/', ShopView.as_view(), name='shop' ),
    path('product/', AllProductsViev.as_view(), name='all_products' ),
    path('product/<slug:slug>/', ProductView.as_view(), name='product' ),
    
    
]