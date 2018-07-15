from django.shortcuts import render
from .models import Quote
import random

# Create your views here.


def home_page(request):
    return render(request, 'home.html', {
        'random_quote': 'Kek' + str(random.randint(1, 1000000000))
    })
