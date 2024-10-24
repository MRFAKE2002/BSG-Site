from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path ('', views.article_list_view, name='article_list'), 
    path ('detail/<slug>', views.ArticleDetail.as_view(), name='article_detail'),
    # path ('search/', views.search_view, name='search'),
]
