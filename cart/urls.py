from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_details_view, name='cart_details'),
    path('add/', views.add_product_to_cart_view, name='add_product_to_cart'),
    path('remove/', views.remove_from_cart_view, name='remove_from_cart'),
    path('clear/', views.clear_cart_view, name='clear_cart'),
]
