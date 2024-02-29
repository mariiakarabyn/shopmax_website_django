from django.contrib import admin
from django.utils.html import format_html

from shopmax.models import Category, Product, Brand, Color, Size, Image

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_products')
    search_fields = ('name',)
    
    @staticmethod
    def total_products(obj):
        count = obj.products.count()
        link = f'/admin/shop/product/?brend_id_exect={obj.id}'
        return format_html(f'<a href="{link}">{count} products</a>')
        
    

admin.site.site_header = 'Django ShopMax'
admin.site.site_title = 'Django ShopMax'
admin.site.index_title = 'Django ShopMax'
admin.site.register(Category)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Image)
admin.site.register(Product)

