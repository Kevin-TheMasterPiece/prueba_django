from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello(request):
    return render(request, 'index.html')
def otro(request):
    return HttpResponse("miuau")
def casco(request):
    return HttpResponse("Helme")
def hola(request):
    return render(request, 'hola.html')
def poque(request):
    return render(request, 'poque.html')

def nose(request):
    return render(request, 'nose.html')