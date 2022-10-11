from django.urls import path
from .views import title, home

urlpatterns = [
    path('', title),
    path('home', home, name='home')
]