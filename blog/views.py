from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.core.paginator import Paginator
from urllib.parse import urlencode
from django.views.generic import ListView, DetailView
from .models import Article, Category, ArticleThumbnails, Tag


class CategoryList(ListView):
    
    model = Category
    template_name = 'blog/category_list.html'


class CategoryList(ListView):
    
    model = Tag
    template_name = 'blog/tag_list.html'


#------------------------------------------------------------------------------------------------------------------------------------#

# class ArticleList(ListView):

#     model = Article
#     template_name = 'blog/article_list.html'

#------------------------------------------------------------------------------------------------------------------------------------#

def article_list_view(request):
    articles = Article.objects.all()
    
    if 'search' in request.GET:
        data = request.GET.get('search')
        if data.isdigit():
            articles = Article.objects.filter(Q(publish__icontains=data))
        else:
            articles = Article.objects.filter(Q(title__icontains=data))
    
    paginator = Paginator(articles, 2)
    
    page_number = request.GET.get('page')
    
    url_data = request.GET.copy()
    
    if 'page' in url_data:
        del url_data['page']
    
    page_obj = paginator.get_page(page_number)
    
    context = {
        'articles' : page_obj,
        'page_number' : page_number,
        'url_data': urlencode(url_data),
    }
    
    return render(request, 'blog/article_list.html', context)


class ArticleDetail(DetailView):

    models = Article
    template_name = 'blog/article_detail.html'
    
    def get_object(self):
    
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article.objects.all(), slug=slug)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        
        context = super().get_context_data(**kwargs)
        context['recent'] = Article.objects.all().order_by('publish')[:3]
        return context    


# @require_POST
# def search_view(request):
#     article_query = Article.objects.all()
#     if request.method == "POST":
#         search = request.POST.get('query')
#         articles = article_query.filter(Q(title__icontains = search) | Q(description__icontains = search))
        
#         return render(request, 'blog/search_result.html', {"articles": articles})
