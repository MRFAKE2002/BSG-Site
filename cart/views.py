from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect

from product.models import Product
from .cart import Cart


def cart_details_view(request):

    cart = Cart(request)
    
    """
        We want to send the cart details in the page.

        'product_information':{
            'id' : {}
            'name' : {}
            'brand' : {}
            'application' : {}
                .
                .
                .
        }

    """
    for item in cart:
        print(item)
    
    context = {
        'cart' : cart
    }
    
    return render(request, 'cart/cart_detail.html', context)


@require_POST
def add_product_to_cart_view(request):
    """
        We use this function to add the product to the cart when user clicks on [add to cart] bottom in product_details.html
    """
    url = request.META.get('HTTP_REFERER')
    # We use this code to redirect user to url that he was

    product_id = request.POST.get('product_id')
    
    product = get_object_or_404(Product, id=product_id)
    
    cart = Cart(request)
    
    cart.add_to_cart(product)

    messages.success(request, "Product added successfully to your cart.", 'success')
    
    return HttpResponseRedirect(url)


@require_POST
def remove_from_cart_view(request):
    
    url = request.META.get('HTTP_REFERER')
    # We use this code to redirect user to url that he was

    cart = Cart(request)

    product_id = request.POST.get('product_id')
    
    cart.remove_from_cart(product_id)

    messages.warning(request, "Product removed successfully from your cart.", 'danger')
    return HttpResponseRedirect(url)


@require_POST
def clear_cart_view(request):
    """
    We use this function to clear the cart by form in cart_detail page
    """
    url = request.META.get('HTTP_REFERER')
    # We use this code to redirect user to url that he was
    
    cart = Cart(request)
    
    cart.clear()
    
    messages.error(request, 'The cart has cleared.')
    
    return HttpResponseRedirect(url)

