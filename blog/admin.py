from django.contrib import admin
import admin_thumbnails
from .models import Category, Tag, Article, ArticleThumbnails


class ArticleImageInline(admin.TabularInline):
    model = ArticleThumbnails
    extra = 1
    fields = ['images']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'parent']
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}


@admin_thumbnails.thumbnail('thumbnail')
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ['title', 'slug', 'category_to_str', 'tag_to_str', 'thumbnail_thumbnail', 'publish'] 
    search_fields = ('title', 'tag', 'slug', 'category')   
    inlines = [ArticleImageInline]


@admin_thumbnails.thumbnail('images')
@admin.register(ArticleThumbnails)
class ArticleThumbnailsAdmin(admin.ModelAdmin):
    list_display = ['images_thumbnail']

