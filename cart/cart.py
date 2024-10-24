"""
    Here we want to make our cart class and we use OOP 
"""

from product.models import Product

class Cart:

    def __init__(self, request):
        """
            We get the request at first because we have different cart for each request and we want to use sessions for each request.
        """
        self.request = request
        
        self.session = request.session
        # Now we got the request`s session from browser and we use it to make new cart for user or if user had car before we can change it.
        
        """
            We want to add a cart in list of data in our request`s session and make a dictionary in the cart 
            to add data of the request in the cart.
            
            Like this:
                session = {
                    'cart' : {
                        product1,
                    }
                }  
        """
        
        cart = self.session.get('cart')
        
        """ 
            At first we must make sure that this session from request had cart before or not  
            So we check that is there any cart in our request`s session or not 
            In above code if there is the cart in our request`s session put it in the cart variable 
            But if there is not any cart in our request`s session put None in the cart variable        
        """
        
        if not cart:
            self.session['cart'] = {}
            # Now we use a if to check that if there isn`t any cart in our request`s session so add a cart in our session
            
            cart = self.session['cart']

            """ 
                We can make this tow above code into one line code 
                Like this:
                    cart = self.session['cart'] = {}
            """
        
        self.cart = cart

#---------------------------------------------------------------------------------------------------------------------#
    
    def add_to_cart(self, product):
        """
            In this method we check if the product is already in the cart or not.
            But if there is no product in the cart then add it to the cart
        """
        
        product_id = str(product.id)
        # We need to get the product`s id to add it in the cart 
        
        """
            Now we must check if the product is not in the cart and add it to the cart.
        """
        
        if product_id not in self.cart:
            self.cart[product_id] = {}
        
        """
                Now our session is like this:
                    session = {
                        'cart' : {
                            'product_id' : {
                                
                            },
                        },
                    }
        """
        
        self.save_session()

#---------------------------------------------------------------------------------------------------------------------#
    
    def remove_from_cart(self, product):
        """
            In this method we remove the product from the cart
        """
        # print(f"Removing from cart - ID: {product.id}")
        # print(f"Current cart: {self.cart}")

        # product_id = str(product.id)

        if product in self.cart:
            del self.cart[product]
            
            self.save_session()
        
        """
                Now our session is like this:
                    session = {
                        'cart' : {
                            
                        },
                    }
        """
        

#---------------------------------------------------------------------------------------------------------------------#
    
    def save_session(self):
        """
            In this method we save the changes to the session
        """
        self.session.modified = True

#---------------------------------------------------------------------------------------------------------------------#

    def __iter__(self):
        
        cart_products_ids = self.cart.keys()

        products_queryset = Product.objects.filter(id__in=cart_products_ids)
        
        cart = self.cart.copy()
        
        for product in products_queryset:
            cart[str(product.id)]['product_information'] = product

        
        """
            Now our session is like this:
                session = {
                    'cart' : {
                        'product_id' : {
                            'product_information':{
                                'name' : {}
                                'brand' : {}
                                'application' : {}
                                    .
                                    .
                                    .
                            }
                        },
                    },
                }
        """


        for item in cart.values():
            
            yield item
            """
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

#---------------------------------------------------------------------------------------------------------------------#

    def __len__(self):
        """
            In this magic method we will show the number of all products in the cart.
        """
        
        return len([items for items in self.cart.values()])

        # Now we want the total product_information of all products in the cart.                

#---------------------------------------------------------------------------------------------------------------------#

    def clear(self):
        """
            In this method we will clear all the cart from session. 
        """
        del self.session['cart']

        
        """
            Now our session is like this:
                session = {
                    'cart' : {
                        
                    },
                }
        """
        
        self.save_session()

#---------------------------------------------------------------------------------------------------------------------#    

