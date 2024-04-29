from django.urls import path
from .views import IndexView, RegularView, ShopView, SigdleBlogView, ProductView, BlogView, CheckoutView, ContactView, AllProductsView

urlpatterns = [
    path('', IndexView.as_view(), name='index' ),
    path('regular/', RegularView.as_view(), name='regular' ),
    path('blog/', BlogView.as_view(), name='blog' ),
    path('single_blog/', SigdleBlogView.as_view(), name='single_blog' ),
    path('checkout/', CheckoutView.as_view(), name='checkout' ),
    path('contact/', ContactView.as_view(), name='contact' ),
    path('shop/<slug:slug>/', ShopView.as_view(), name='shop' ),
    path('product/', AllProductsView.as_view(), name='all_products' ),
    path('product/<slug:slug>/', ProductView.as_view(), name='product' ),
    
    
]