from django.urls import path
from .views import start, home

urlpatterns = [
    path('test/', start),
    path('home', home, name='home')
]