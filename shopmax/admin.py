from django.contrib import admin

from shopmax.models import Category, Product, Brand, Color, Size, Image

admin.site.site_header = 'Django ShopMax'
admin.site.site_title = 'Django ShopMax'
admin.site.index_title = 'Django ShopMax'
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Image)
admin.site.register(Product)

