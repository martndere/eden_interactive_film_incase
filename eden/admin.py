from django.contrib import admin
from .models import Clip, Choice

@admin.register(Clip)
class ClipAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'prompt_time')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    list_filter = ('created_at',)
    fieldsets = (
        (None, {'fields': ('name', 'slug', 'description', 'video', 'thumbnail')}),
        ('Prompt & Metadata', {'fields': ('prompt_time', 'audio_prompt', 'extra_notes')}),
    )

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('from_clip', 'label', 'to_clip', 'order')
    list_filter = ('from_clip',)
    ordering = ('from_clip', 'order')
