from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
import json
from uuid import uuid4

from .services import create_image_from_prompt, download_image_from_url
from .models import GeneratedAsset
from apps.eden.models import Clip

# Create your views here.
@login_required
@require_POST
def generate_image_view(request):
    try:
        data = json.loads(request.body)
        prompt = data.get('prompt')
        clip_slug = data.get('clip_slug')

        if not prompt:
            return JsonResponse({'error': 'Prompt is required.'}, status=400)

        openai_image_url = create_image_from_prompt(prompt)
        image_content = download_image_from_url(openai_image_url)

        source_clip = Clip.objects.filter(slug=clip_slug).first()

        asset = GeneratedAsset(user=request.user, prompt=prompt, source_clip=source_clip)
        file_name = f"{request.user.username}_{uuid4().hex}.png"
        asset.generated_image.save(file_name, image_content, save=True)

        return JsonResponse({'image_url': asset.generated_image.url})
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=503)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
