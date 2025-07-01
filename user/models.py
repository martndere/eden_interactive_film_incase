from django.db import models
from django.contrib.auth.models import User

class UserFilm(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.user.username}"

class UserClip(models.Model):
    film = models.ForeignKey(UserFilm, on_delete=models.CASCADE, related_name='clips')
    name = models.CharField(max_length=200)
    video = models.FileField(upload_to='user_clips/')
    thumbnail = models.ImageField(upload_to='user_thumbnails/', blank=True)
    narrative = models.TextField(blank=True)
    prompt_time = models.FloatField(default=0)
    audio_prompt = models.FileField(upload_to='user_audio_prompts/', blank=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.film.title})"

class UserChoice(models.Model):
    from_clip = models.ForeignKey(UserClip, on_delete=models.CASCADE, related_name='choices_from')
    to_clip = models.ForeignKey(UserClip, on_delete=models.CASCADE, related_name='choices_to')
    label = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.label} ({self.from_clip.name} → {self.to_clip.name})"