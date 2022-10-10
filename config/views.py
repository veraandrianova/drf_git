from django.shortcuts import render, redirect


# Create your views here.
def start(request):
    return render(request, 'config/test.html')

def home(request):
    print(request)
    return render(request, 'config/home.html')