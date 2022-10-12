from rest_framework import serializers

from .models import SocialLink, UseTools, User, Account
from .services import check_repo, get_email


class UseToolsSerializers(serializers.ModelSerializer):
    '''Языки программирования'''

    class Meta:
        model = UseTools
        fields = '__all__'


class LinkCreateSerializers(serializers.ModelSerializer):
    '''Добавление ссылки'''
    use_tools = UseToolsSerializers(read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SocialLink
        fields = ('title', 'description', 'use_tool', 'link', 'use_tools', 'user')

    # def create(self, validated_data):
    #     print(validated_data)
    #     # cur_user = validated_data.get('user', None)
    #     # try:
    #     #     user = AuthUser.objects.get(nick_git=cur_user)
    #     # except AuthUser.DoesNotExist:
    #     #     email, name = get_email(cur_user)
    #     #     user = AuthUser.objects.create(
    #     #         email=email,
    #     #         firstname=name,
    #     #         nickname=cur_user,
    #     #         nick_git=cur_user
    #     #     )
    #
    #     # user = AuthUser.objects.get(id='2')
    #     print(self.request.user)
    #     link = SocialLink.objects.create(
    #         title=validated_data.get('title', None),
    #         description=validated_data.get('description', None),
    #         use_tool=validated_data.get('use_tool', None),
    #         user=user
    #     )
    #     return link


