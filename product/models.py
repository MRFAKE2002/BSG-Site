from django.db import models
from django.urls import reverse

from taggit.managers import TaggableManager


class BaseModel(models.Model):
    datetime_created = models.DateTimeField(auto_now_add=True)
    
    datetime_updated = models.DateTimeField(auto_now=True)
    
    is_active = models.BooleanField(default=True)


class Content(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='product_contents')
    
    name = models.CharField(max_length=255, blank=True, null=True)
    
    content = models.TextField()


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Industry(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Industry'
        verbose_name_plural = 'Industries'


class Application(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    
    slug = models.SlugField(max_length=255, unique=True)
    
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True, blank=True, related_name='products')
    
    industry = models.ForeignKey(Industry, on_delete=models.PROTECT, null=True, blank=True, related_name='products')
    
    description = models.TextField(blank=True, null=True)
    
    technical_information = models.TextField(null=True, blank=True)
    
    application = models.ForeignKey(Application, on_delete=models.PROTECT, related_name='products')
    # application = models.ManyToManyField(Application, related_name='products')
    
    type = models.ForeignKey(Type, on_delete=models.PROTECT, related_name='products')
    # type = models.ManyToManyField(Type, related_name='products')
    
    image = models.ImageField(upload_to='images/products/')
    
    product_pdf = models.FileField(upload_to='products/product_pdf/', blank=True, null=True)
    
    similar_tags = TaggableManager(blank=True)

    def __str__(self):
        return f'id: {self.id} | name: {self.name}'

    def get_absolute_url(self):
        return reverse("product:product_detail", kwargs={"slug": self.slug})


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="product_images")
    
    content = models.TextField(null=True, blank=True)
    
    image = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = 'ProductImage'
        verbose_name_plural = 'ProductImages'
