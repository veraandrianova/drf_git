from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.User)
class AdminUser(admin.ModelAdmin):
    list_display = ('username', )


@admin.register(models.SocialUserLink)
class AdmimnSocialUserLink(admin.ModelAdmin):
    list_display = ('user', 'link')

@admin.register(models.UseTools)
class AdminUseTools(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(models.Account)
class AdminAccount(admin.ModelAdmin):
    list_display = ('user', 'nickname_git', 'email', )