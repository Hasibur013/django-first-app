from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("Hello Django!")
    teacher = {'name': 'Hasibur', 'course': 'Django'}
    return render(request, 'index.html', teacher)

def aishop(request):
    return HttpResponse("Hello AI shop!")