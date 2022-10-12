from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .models import SocialLink, Account
from .permissions import IsOwnerOrReadOnly
from .serializer import LinkCreateSerializers
from .services import check_repo


# Create your views here.
def title(request):
    return render(request, 'config/title.html')


class CreateLink(viewsets.ModelViewSet):
    '''Добавление ссылки'''
    queryset = SocialLink.objects.all()
    serializer_class = LinkCreateSerializers

    def create(self, request, *args, **kwargs):
        print('req', request.user)
        try:
            cur_user = Account.objects.get(user_id=request.user.id)
            print('cur', cur_user)
        except Account.DoesNotExist:
            print('no')
            return render(request, 'config/title.html')
        if cur_user:
            serializer = self.get_serializer(data=request.data)
            print(serializer)
            repo = check_repo(self.request, cur_user)
            print(repo)
            if repo:
                print('ok')
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_permissions(self):
        if self.action == 'list' or 'retrieve':
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsOwnerOrReadOnly]
        return [permission() for permission in permission_classes]

    # def perform_create(self, serializer):
    #     repo = check_repo(self.request)
    #     if repo:
    #         print('yes')
    #         serializer.save()
    #     else:
    #         return Response(status=status.HTTP_404_NOT_FOUND)

    def perform_update(self, serializer):
        serializer.save()