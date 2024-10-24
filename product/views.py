from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.http import FileResponse
from django.contrib import messages
from django.core.paginator import Paginator
from urllib.parse import urlencode

from .models import Product, Brand, Industry, ProductImages
from .forms import SearchForm
from .filters import ProductFilter


def product_list_view(request):
    products = Product.objects.filter(is_active=True)
    
    form = SearchForm()
    
    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            data = form.cleaned_data['search']
            if data.isdigit():
                messages.error(request, 'It must be character a-z, A-Z', 'danger')
                return render(request, 'product/product_list.html', {"products": products})
            else:
                products = Product.objects.filter(Q(name__icontains=data))
    
    f = ProductFilter(request.GET, queryset=products)
    
    products = f.qs
    
    paginator = Paginator(products, 3)
    
    page_number = request.GET.get('page')
    
    url_data = request.GET.copy()
    
    if 'page' in url_data:
        del url_data['page']
    
    page_obj = paginator.get_page(page_number)
    
    # for field in f.form:
    #     print(field)
    
    context = {
        'products' : page_obj,
        'page_number' : page_number,
        'filter':f,
        'url_data': urlencode(url_data),
        'form':form,
    }
    
    return render(request, 'product/product_list.html', context)


def product_detail_view(request, slug):
    product = get_object_or_404(
        Product.objects.select_related('type', 'application').prefetch_related('product_contents'),
        slug= slug
    )
    
    product_images = ProductImages.objects.filter(product__slug = slug)
    
    similar_products = product.similar_tags.similar_objects()[:5]
    
    
    if product.type.name == 'Product':
        
        products = Product.objects.select_related('type', 'application').filter(type=1)[:5]
        
        context = {
            'product': product,
            'product_images': product_images,
            'similar_products': similar_products,
            'products': products,
        }
        
        return render(request, 'product/product_detail.html', context)
    
    elif product.type.name == 'Solution':
        solutions = Product.objects.select_related('type', 'application').filter(type=2)[:5]
        
        context = {
            'product': product,
            'product_images': product_images,
            'similar_products': similar_products,
            'solutions': solutions,
        }
        
        return render(request, 'product/solution_detail.html', context)
    
    services = Product.objects.select_related('type', 'application').filter(type=3)[:5]
    
    context = {
        'product': product,
        'product_images': product_images,
        'similar_products': similar_products,
        'services': services,
    }
    
    return render(request, 'product/service_detail.html', context)


def download_pdf_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if product.product_pdf:
        return FileResponse(product.product_pdf, as_attachment=True)


def search_view(request):
    search = SearchForm(request.POST)
    if search.is_valid():
        data = search.cleaned_data['search']
        if data.isdigit():
            messages.error(request, 'It must be character a-z, A-Z', 'danger')
            return render(request, 'product/product_list.html', {"products": products})
        else:
            products = Product.objects.filter(Q(name__icontains=data))

            f = ProductFilter(request.GET, queryset=products)

            products = f.qs
            
            paginator = Paginator(products, 3)
            
            page_number = request.GET.get('page')
            
            url_data = request.GET.copy()
            
            if 'page' in url_data:
                del url_data['page']
            
            page_obj = paginator.get_page(page_number)
            
            context = {
                'products' : page_obj,
                'page_number' : page_number,
                'filter':f,
                'url_data': urlencode(url_data)
            }
            
            return render(request, 'product/product_list.html', context)
    else:
        return redirect('product:product_list' )

