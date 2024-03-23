from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def beranda(request):
    return render(request, 'beranda.html')