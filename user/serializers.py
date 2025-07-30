# user/serializers.py
from rest_framework import serializers
from .models import UserClip

class UserClipSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClip
        fields = '__all__'