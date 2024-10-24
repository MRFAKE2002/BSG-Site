from django.shortcuts import render



def about_us_view(request):
    
    context = {}
    
    return render(request, 'page/about_us.html/', context)


def home_view(request):
    
    context = {}
    
    return render(request, 'page/home.html', context)


def contact_us_view(request):
    
    context = {}
    
    return render(request, 'page/contact_us.html', context)


def oneweb_preorder_view(request):
    
    context = {}
    
    return render(request, 'page/oneweb_preorder.html', context)


def air_view(request):
    
    context = {}
    
    return render(request, 'page/air.html', context)


def land_view(request):
    
    context = {}
    
    return render(request, 'page/land.html', context)


def marine_view(request):
    
    context = {}
    
    return render(request, 'page/marine.html', context)


def our_planet_view(request):
    
    context = {}
    
    return render(request, 'page/our_planet.html', context)
