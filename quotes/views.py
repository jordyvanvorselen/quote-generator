from django.shortcuts import render, render_to_response
import random
import requests

# Create your views here.


def home_page(request):
    response = requests.get('https://talaikis.com/api/quotes/random/')
    response_content = response.json()
    quote = response_content["quote"]
    author = response_content["author"]
    response = render_to_response('home.html', {
        'random_quote': quote,
        'author': author
    })
    return response
