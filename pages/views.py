from django.shortcuts import render
from listings.choices import price_choices, bedrooms_choices, state_choices
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.

def home(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedrooms_choices' : bedrooms_choices,
        'price_choices' : price_choices
    }
    return render(request, 'pages/home.html', context)

def about(request):
     #Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')

    #Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors':realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html',context)