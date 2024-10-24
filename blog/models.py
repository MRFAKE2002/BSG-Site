from django.db import models
from django.utils import timezone
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):

    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Sub Category', \
                                related_name='sub', default=None, null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Tag(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title


class Article(models.Model):

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.ManyToManyField(Category, verbose_name="Category", related_name='cats')
    tag = models.ManyToManyField(Tag, verbose_name="Tags", related_name='tags')
    description = CKEditor5Field(config_name='extends')
    thumbnail = models.ImageField(upload_to='images')
    publish =  models.DateTimeField(default=timezone.now, verbose_name='Publication time')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def category_to_str(self):
        return " - ".join([category.title for category in self.category.all()])

    def tag_to_str(self):
        return " - ".join([tag.title for tag in self.tag.all()])
        
    def get_absolute_url(self):
        return reverse("blog:article_detail", kwargs={"slug": self.slug})
    

class ArticleThumbnails(models.Model):

    article = models.ForeignKey("Article", verbose_name="Article Images", on_delete=models.CASCADE, related_name='article_images')
    images = models.ImageField(upload_to='images')
