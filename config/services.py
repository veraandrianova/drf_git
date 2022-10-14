from django_filters import rest_framework as filters
import requests

from .models import SocialUserLink, Account
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from allauth.socialaccount.models import SocialAccount# step 3 made this possible


@receiver(post_save, sender=SocialAccount)
def create_profile(sender, instance, created, **kwargs):
    print(sender)
    print(instance.id)
    print(instance)
    print(instance.extra_data['login'])
    print(instance.extra_data['url'])
    print(instance.extra_data['name'])
    print(instance.extra_data['email'])
    try:
        user = User.objects.get(username=instance)
        print(user)
    except User.DoesNotExist:
        pass
        # user = User.objects.create(username=instance, )
    try:
        cur_user = Account.objects.get(user_id=user.id)
        print('ok')
    except Account.DoesNotExist:
        cur_user = Account.objects.create(user_id=user.id,
                                          nickname_git=instance.extra_data['login'],
                                          email=(instance.extra_data['email'], None),
                                          url=instance.extra_data['url'])
        print('create_new')
    return cur_user

def get_path_upload_avatar(instance, file):
    '''Постоение пути к файлуб format: (media)/avatar/user_id/photo.jpg'''
    return f'avatar/{instance.id}/{file}'


def get_user_repos(username):
    '''Поиск всех репозиторие пользователя'''
    user_info = requests.get(f'https://api.github.com/users/{username}/repos')
    repos = user_info.json()
    user_repos = []
    for repo in repos:
        r = repo.get('name')
        user_repos.append(r)
    return user_repos


def check_repo(request, cur_user):
    '''Поиск добавляемого репозитория у пользователя'''
    print('r', request)
    cur_repo = request.data.get('link').split('/')[-1]
    username = cur_user
    print(cur_repo)
    print(username)
    user_repo = get_user_repos(username)
    if cur_repo in user_repo:
        return True


def get_email(cur_user):
    '''Поиск email и имя пользователя'''
    user_info = requests.get(f'https://api.github.com/users/{cur_user}/events/public')
    info = user_info.json()[0].get('payload').get('commits')[0]
    email = info.get('author').get('email')
    name = info.get('author').get('name')
    return email, name


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class UseToolFilter(filters.FilterSet):
    use_tool = CharFilterInFilter(field_name='use_tool__name', lookup_expr='in')

    class Meta:
        model = SocialUserLink
        fields = ['use_tool', ]
