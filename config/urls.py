from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include


urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path("admin/", admin.site.urls),
    path('', include('shopmax.urls')),
    path('', include('website.urls'))
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

