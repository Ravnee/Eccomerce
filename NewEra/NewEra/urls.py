
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include('NEapp1.urls')),
    path('home2/',include('NEapp2.urls')),  
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
