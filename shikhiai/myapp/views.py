from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Contact

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
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        values = Contact(name=name, email=email, desc=desc)
        values.save()
    return render(request, 'contact.html', {'current_page': 'contact'})