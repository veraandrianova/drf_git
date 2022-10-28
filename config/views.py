from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import SocialUserLink, Account, User
from .permissions import IsOwnerOrReadOnly
from .serializer import LinkCreateSerializers, UserProfileSerializers
from .services import check_repo, get_email, UseToolFilter


# Create your views here.

def title(request):
    return render(request, 'config/title.html')


class CreateLink(viewsets.ModelViewSet):
    '''Добавление ссылки'''
    queryset = SocialUserLink.objects.all()
    serializer_class = LinkCreateSerializers
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UseToolFilter

    def create(self, request, *args, **kwargs):
        try:
            cur_user = Account.objects.get(user_id=request.user.id)
        except Account.DoesNotExist:
            return render(request, 'config/title.html')
        if cur_user:
            serializer = self.get_serializer(data=request.data)
            repo = check_repo(self.request, cur_user)
            if repo:
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                # return Response({'error': 'Not found repo'}, status=status.HTTP_400_BAD_REQUEST)
                return APIException(detail='Not found error', code=status.HTTP_400_BAD_REQUEST)
    def get_permissions(self):
        if self.action == 'list' or 'retrieve':
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]

    def perform_update(self, serializer):
        serializer.save()


class UserProfile(viewsets.ModelViewSet):
    '''Добавление ссылки'''
    queryset = User.objects.all()
    serializer_class = UserProfileSerializers

    def get_permissions(self):
        if self.action == 'list' or 'retrieve':
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]
