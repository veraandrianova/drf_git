from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import title, CreateLink, UserProfile

links = CreateLink.as_view({
    'get': 'list',
    'post': 'create'
})

detail_link = CreateLink.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

users = UserProfile.as_view({
    'get': 'list',
    'post': 'create'
})

detail_user = UserProfile.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    path('links/', links, name='links'),
    path('links/<int:pk>/', detail_link, name='detail_link'),
    path('users/', users, name='users'),
    path('users/<int:pk>/', detail_user, name='detail_user'),
    path('', title),
])
