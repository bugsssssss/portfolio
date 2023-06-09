from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['skills', 'experience', 'additional']


@admin.register(Callback)
class CallbackAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'topic']


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(BotUsers)
class BotUsersAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username']


@admin.register(ProjectsDecription)
class ProjectsDecriptionAdmin(admin.ModelAdmin):
    list_display = ['text']


