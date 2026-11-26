from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Materialverwaltung Prototyp index view")
# Create your views here.
