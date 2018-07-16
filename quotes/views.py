from django.shortcuts import render, render_to_response
import wikiquote
import random

# Create your views here.


def home_page(request):
    quote = random.choice(wikiquote.quotes(
        page_title='Marcus Aurelius', lang='en'))
    response = render_to_response('home.html', {
        'random_quote': quote,
        'author': 'Marcus Aurelius'
    })
    return response
