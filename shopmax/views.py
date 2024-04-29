from django.shortcuts import get_object_or_404
from django.db.models import Prefetch
from django.views.generic import TemplateView, ListView

from . models import Category, Product, Brand, Image


class RegularView(TemplateView):
    template_name = 'regular-page.html'
    
class SigdleBlogView(TemplateView):
    template_name = 'single-blog.html'

class BlogView(TemplateView):
    template_name = 'blog.html'

class CheckoutView(TemplateView):
    template_name = 'checkout.html'
    
class ContactView(TemplateView):
    template_name = 'contact.html'
    
class AllProductsView(ListView):
    template_name = 'shop.html'
    model = Product
    context_object_name = 'products'
    slug_url_kwarg = 'slug'
    paginate_by = 9
    
    def get_queryset(self):
        return  Product.objects.prefetch_related(
        Prefetch('images', 
                 queryset=Image.objects.order_by('-size'))
        )
        
class ProductView(TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        single_product = get_object_or_404(Product, slug=self.kwargs.get('slug'))
        main_images = Image.objects.filter(product=single_product).order_by('-size')[:4]
        context['product'] = single_product
        context['main_images'] = main_images
        return context

class ShopView(ListView):
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 9

    def get_queryset(self):
        category_slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=category_slug)
        return Product.objects.filter(categories=category).prefetch_related(
            Prefetch('images', queryset=Image.objects.order_by('-size'))
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('slug')
        category = get_object_or_404(Category, slug=category_slug)
        context['category_name'] = category.name
        return context
    

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_name = self.request.GET.get('category')
        slug = self.kwargs.get('slug')

        if category_name:
            category = get_object_or_404(Category, name=category_name)
            products = Product.objects.filter(categories=category).prefetch_related(
                Prefetch('images', queryset=Image.objects.order_by('-size'))
            )[:9]
        elif slug:
            category = get_object_or_404(Category, slug=slug)
            products = Product.objects.filter(categories=category).prefetch_related(
                Prefetch('images', queryset=Image.objects.order_by('-size'))
            )[:9]
        else:
            products = Product.objects.all().prefetch_related(
                Prefetch('images', queryset=Image.objects.order_by('-size'))
            )[:5]

        brands = Brand.objects.all()[3:9]
        context['brands'] = brands
        context['products'] = products
        return context