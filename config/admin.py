from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.AuthUser)
class AdminAuthUser(admin.ModelAdmin):
    list_display = ('id', 'email', 'nickname')

@admin.register(models.SocialLink)
class SocialLinkAuthUser(admin.ModelAdmin):
    list_display = ('user', 'link')