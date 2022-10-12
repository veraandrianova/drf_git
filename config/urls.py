from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import title, CreateLink

links = CreateLink.as_view({
    'get': 'list',
    'post': 'create'
})

detail_link = CreateLink.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('links/', links, name='links'),
    path('links/<int:pk>/', detail_link, name='detail_link'),
    path('', title),
])