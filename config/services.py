from django_filters import rest_framework as filters
import requests

from .models import SocialUserLink


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


# def check_user_account(user):
#     cur_user = Account.objects.get(user_id=user.id)
#     return cur_user

# def check_user(user):
#     cur_user = User.objects.get(id=user.id)
#     return cur_user

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class UseToolFilter(filters.FilterSet):
    use_tool = CharFilterInFilter(field_name='use_tool__name', lookup_expr='in')

    class Meta:
        model = SocialUserLink
        fields = ['use_tool', ]
