from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    return render(request, 'home.html', {'current_page': 'home'})
def home(request):
    return render(request, 'home.html', {'current_page': 'home'})

def blog(request):
    return render(request, 'blog.html', {'current_page': 'blog'})

def about(request):
    return render(request, 'about.html', {'current_page': 'about'})

def contact(request):
    return render(request, 'contact.html', {'current_page': 'contact'})