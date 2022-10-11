from django.shortcuts import render, redirect


# Create your views here.
def title(request):
    return render(request, 'config/title.html')

def home(request):
    print(request.user)
    print(request.auth)
    return render(request, 'config/home.html')