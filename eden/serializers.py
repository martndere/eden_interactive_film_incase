from rest_framework import serializers
from .models import Clip

class ClipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clip
        fields = ['id', 'title', 'slug', 'description', 'video_file']
