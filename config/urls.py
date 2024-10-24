"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    # Django Admin Urls
    path('admin/', admin.site.urls),

    # # Django Tool-Bar Urls
    # path("__debug__/", include("debug_toolbar.urls")),

    # Product App Urls
    path('products/', include('product.urls', namespace='product')),

    # Blog App Urls
    path('blog/', include('blog.urls', namespace='blog')),

    # Cart App Urls
    path('cart/', include('cart.urls', namespace='cart')),

    # Pages App Urls
    path('', include('pages.urls', namespace='pages')),

    # Django Ckeditor-5 Urls
    path("ckeditor5/", include('django_ckeditor_5.urls'), name="ck_editor_5_upload_file"),

]

# serve static and media files from development server
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

