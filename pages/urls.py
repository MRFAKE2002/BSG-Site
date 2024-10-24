from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about-us/', views.about_us_view, name='about_us'),
    path('contact-us/', views.contact_us_view, name='contact_us'),
    path('oneweb-preorder/', views.oneweb_preorder_view, name='oneweb-preorder'),
    path('land/', views.land_view, name='land'),
    path('air/', views.air_view, name='air'),
    path('marine/', views.marine_view, name='marine'),
    path('our-planet/', views.our_planet_view, name='our_planet'),
]
