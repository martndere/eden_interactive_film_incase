from django.contrib import admin
from .models import UserFilm, UserClip, UserChoice

@admin.register(UserFilm)
class UserFilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', 'is_public')
    search_fields = ('title', 'user__username')

@admin.register(UserClip)
class UserClipAdmin(admin.ModelAdmin):
    list_display = ('name', 'film', 'order')
    search_fields = ('name', 'film__title')

@admin.register(UserChoice)
class UserChoiceAdmin(admin.ModelAdmin):
    list_display = ('from_clip', 'label', 'to_clip', 'order')
    list_filter = ('from_clip',)
    ordering = ('from_clip', 'order')