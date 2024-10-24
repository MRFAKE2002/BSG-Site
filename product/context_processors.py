from .models import Product


def product(request):
    """
        In this function, we make a context_processors it means you can have access to products queryset in all templates and you can iterate through it
    """
    return {'products_queryset' : Product.objects.select_related('brand', 'type').all()[:7]}

