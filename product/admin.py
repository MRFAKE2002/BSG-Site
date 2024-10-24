from django.contrib import admin
from django.db.models import Count, Subquery, OuterRef
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from .models import Content, Product, Brand, Industry, Application, Type, ProductImages

import admin_thumbnails


@admin_thumbnails.thumbnail('image')
class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    fields = ('image', 'image_thumbnail', 'content')
    extra = 0


class ContentInline(admin.TabularInline):
    model = Content
    fields = ('name', 'content')
    extra = 0


@admin.register(Product)
@admin_thumbnails.thumbnail('image')
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_thumbnail', 'product_pdf', 'name', 'type', 'application', 'brand', 'industry', 'is_active', 'product_images_count_column', 'product_content_count_column']
    
    search_fields = ['name', 'description', 'technical_information']
    
    prepopulated_fields = {
        'slug' : ['name']
    }
    
    list_editable = ['is_active']
    
    list_filter = ['datetime_created', 'brand', 'industry', 'application', 'type', 'is_active']
    
    list_per_page = 10
    
    list_select_related = ['brand', 'industry']

    ordering = ['id', 'datetime_created', 'name']

    autocomplete_fields = ['brand', 'industry']
    
    inlines = [
        ProductImagesInline,
        ContentInline,
    ]
    
    def get_queryset(self, request):
        # Annotate with counts of related ProductImage instances and ProductVariant instances
        queryset = super().get_queryset(request).annotate(
            product_images_count=Subquery(
                ProductImages.objects.filter(product_id=OuterRef('id')).values('product_id').annotate(
                    count=Count('product_id')).values('count'),
                output_field=models.IntegerField()
            ),
            product_content_count=Subquery(
                Content.objects.filter(product_id=OuterRef('id')).values('product_id').annotate(
                    count=Count('product_id')).values('count'),
                output_field=models.IntegerField()
            ),
        )
        return queryset
    
    
    @admin.display(ordering="product_images_count", description="# images")
    def product_images_count_column(self, product=Product):
        """
            We use this method to get the number of product`s images in the changelist.
        """
        url = (
            reverse("admin:product_productimages_changelist")
            + "?"
            + urlencode({
                "product" : product.id,
            })
        )
        return format_html('<a href="{}" >{}</a>', url, product.product_images_count)
    
    
    @admin.display(ordering="product_content_count", description="# contents")
    def product_content_count_column(self, product=Product):
        """
            We use this method to get the number of product`s content in the changelist.
        """
        url = (
            reverse("admin:product_content_changelist")
            + "?"
            + urlencode({
                "product" : product.id,
            })
        )
        return format_html('<a href="{}" >{}</a>', url, product.product_content_count)



@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    search_fields = ['name']
    
    list_per_page = 10


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    search_fields = ['name']
    
    list_per_page = 10


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    search_fields = ['name']
    
    list_per_page = 10


@admin.register(Industry)
class IndustryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    
    search_fields = ['name']
    
    list_per_page = 10


@admin.register(ProductImages)
@admin_thumbnails.thumbnail('image')
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image_thumbnail']
    
    search_fields = ['content']
    
    list_select_related = ['product']
    
    list_per_page = 10


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'name', 'content']
    
    search_fields = ['name', 'content']
    
    list_select_related = ['product']
    
    list_per_page = 10


