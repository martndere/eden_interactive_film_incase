from django.db import models
from django.contrib.auth.models import User
from apps.eden.models import Clip

# Create your models here.
class GeneratedAsset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='generated_assets')
    source_clip = models.ForeignKey(Clip, on_delete=models.SET_NULL, null=True, blank=True, related_name='generated_assets')
    prompt = models.TextField()
    generated_image = models.ImageField(upload_to='generated_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Asset for {self.user.username} from prompt: "{self.prompt[:30]}..."'
