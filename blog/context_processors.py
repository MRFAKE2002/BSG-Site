from .models import Category, Tag, Article


def category(request):
    context = {
        'categories': Category.objects.select_related('parent').prefetch_related('cats')
    }
    return context


def tag(request):
    context = {
        'tags': Tag.objects.all().prefetch_related('tags')
    }
    return context


def recent_articles(request):
    context = {
        'recent': Article.objects.all().order_by('publish')[:6]
    }
    return context
