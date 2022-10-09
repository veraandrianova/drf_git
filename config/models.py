from django.core.validators import FileExtensionValidator
from django.db import models

from .services import get_path_upload_avatar


# Create your models here.
class AuthUser(models.Model):
    '''Модель пользователя'''
    email = models.EmailField(max_length=150, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg'])]
    )

    @property
    def is_authenticated(self):
        return True

    def __str__(self):
        return self.email

class SocialLink(models.Model):
    '''Модель сылок на проекты git_hub'''
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='social_link')
    link = models.URLField(max_length=100)

    def __str__(self):
        return f'{self.user}'