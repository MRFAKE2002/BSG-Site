from .cart import Cart


def cart(request):
    """
        In this function, we make a context_processors it means you can have access to cart in all templates and you can iterate through it
        So for example in header.html in cart icon you can show the length of all products in the cart
        And you can iterate through it :
            'item' : {
                'product_information' : {
                    'id' : product_id,
                    'name' : product_name,
                        .
                        .
                        .   
                },
            },
    """
    return {'cart' : Cart(request)}

