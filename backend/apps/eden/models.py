from django.db import models
from django.urls import reverse
import uuid

class Clip(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to='clips/')
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_start_clip = models.BooleanField(default=False, help_text="Set to True for the very first clip of the film.")
    prompt_time = models.FloatField(default=0.0, help_text="Time (in seconds) to show choices or prompt")
    audio_prompt = models.FileField(upload_to='audio_prompts/', blank=True, null=True)
    extra_notes = models.TextField(blank=True, help_text="Internal notes or script directions")
    transcript = models.TextField(blank=True, help_text="Auto-generated transcript of the clip's audio.")
    def __str__(self):
        return self.name

class Choice(models.Model):
    from_clip = models.ForeignKey(Clip, related_name='choices', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    to_clip = models.ForeignKey(Clip, related_name='incoming_choices', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='choices/', blank=True)
    order = models.PositiveIntegerField(default=0, help_text="Order to display choices")

    def __str__(self):
        return f"{self.from_clip.name} → {self.label}"