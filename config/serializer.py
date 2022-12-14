from rest_framework import serializers

from .models import SocialUserLink, UseTools, User


class UseToolsSerializers(serializers.ModelSerializer):
    '''Языки программирования'''

    class Meta:
        model = UseTools
        fields = ('name', )


class LinkCreateSerializers(serializers.ModelSerializer):
    '''Добавление ссылки'''
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SocialUserLink
        fields = ('title', 'description', 'use_tool', 'link', 'user')


class UserProfileSerializers(serializers.ModelSerializer):
    '''Добавление ссылки'''

    use_tool = UseToolsSerializers(read_only=True)
    class Meta:
        model = User
        fields = ('username', 'use_tool', )