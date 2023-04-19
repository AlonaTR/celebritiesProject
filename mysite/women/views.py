
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from .models import *

menu=[
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Add page', 'url_name': 'add_page'},
    {'title': 'Contact', 'url_name': 'contact'},
    {'title': 'Login', 'url_name': 'login'}
]
def index(request):
    context = {
        'menu': menu,
        'title': 'General page', 
        'cat_selected': 0,
    }
    return render(request, 'women/index.html',context=context)

def about(request):
    return render(request, 'women/about.html', {'title': 'Страница о сайте'})

def addpage(request):
    return HttpResponse("Add page")

def contact(request):
    return HttpResponse("Contact")

def login(request):
    return HttpResponse("Login")

def post_detail(request, post_id):
    return HttpResponse(f"Post number {post_id}")

def show_category(request, category_id):

    context = {
        'menu': menu,
        'title': 'General page',
        'cat_selected': category_id,
    }
    return render(request, 'women/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')