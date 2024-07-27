from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(reqest):
    return HttpResponse("Hello Django!")

def aishop(reqest):
    return HttpResponse("Hello AI shop!")