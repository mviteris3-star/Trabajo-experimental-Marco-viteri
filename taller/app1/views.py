from django.shortcuts import render

# Create your views here.

def presentar(request):
    return render(request, 'base.html')
