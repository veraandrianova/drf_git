from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models

# from .services import get_path_upload_avatar

class User(AbstractUser):

    def __str__(self):
        return self.username

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_account')
    nickname_git = models.CharField(max_length=100)
    email = models.EmailField(max_length=150, unique=True)

    def __str__(self):
        return self.nickname_git


class UseTools(models.Model):
    name = models.CharField('Язык программирования', max_length=70, db_index=True)

    def __str__(self):
        return self.name


class SocialUserLink(models.Model):
    '''Модель ссылок на проекты git_hub'''
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_link')
    title = models.CharField('Название', max_length=150)
    description = models.TextField('Описание', default='Описание отсутствует')
    use_tool = models.ForeignKey(UseTools, on_delete=models.CASCADE, related_name='user_tool_social_link', default=1)
    link = models.URLField(max_length=100)

    def __str__(self):
        return f'{self.user}'
