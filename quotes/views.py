from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'home.html', {
        'random_quote': 'Goals transform a random walk into a chase.'
    })
