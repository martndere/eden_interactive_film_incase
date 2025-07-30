# Core Django
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils.text import slugify

# Django REST Framework
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

# Project-specific
from .models import Clip, Choice
from .serializers import ClipSerializer

# ----------------------------
# Web views (HTML rendering)
# ----------------------------

def home(request):
    return render(request, 'eden/home.html')

def clip_a_view(request):
    clip = Clip.objects.filter(name__icontains="Clip A").first()
    choices = clip.choices.all() if clip else []
    return render(request, 'eden/clip_a.html', {'clip': clip, 'choices': choices})

def clip_detail(request, slug):
    template_slug = slug.replace('-', '_')
    clip = get_object_or_404(Clip, slug=slug)
    choices = clip.choices.all()
    return render(request, f'eden/{template_slug}.html', {'clip': clip, 'choices': choices})

def branch_view(request, character):
    mapping = {
        'ralph': 'clip-c',
        'taika': 'clip-f',
        'tpma': 'clip-q',
    }
    slug = mapping.get(character)
    if not slug:
        return HttpResponse("Unknown character", status=404)
    return redirect('clip_detail', slug=slug)

def clip_list_partial(request):
    q = request.GET.get('q', '')
    clips = Clip.objects.all()  # (You could filter by q if needed)
    return render(request, 'eden/partials/clip_list_partial.html', {'clips': clips})

# ----------------------------
# API views
# ----------------------------

@api_view(['GET'])
def clip_list_api(request):
    clips = Clip.objects.all()
    serializer = ClipSerializer(clips, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def clip_detail_api(request, slug):
    clip = Clip.objects.filter(slug=slug).first()
    if clip:
        serializer = ClipSerializer(clip)
        return Response(serializer.data)
    return Response({'error': 'Clip not found'}, status=404)

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def upload_clip(request):
    title = request.data.get('title')
    description = request.data.get('description', '')
    video_file = request.FILES.get('video_file')

    if not title or not video_file:
        return Response({'error': 'Title and video_file are required'}, status=400)

    clip = Clip.objects.create(
        title=title,
        description=description,
        slug=slugify(title),
        video_file=video_file
    )
    serializer = ClipSerializer(clip)
    return Response({'message': 'Clip uploaded', 'clip': serializer.data})

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def delete_clip(request, clip_id):
    clip = get_object_or_404(Clip, id=clip_id)
    clip.delete()
    return Response({'message': 'Clip deleted'})

# ----------------------------
# DRF ViewSet
# ----------------------------

class ClipViewSet(viewsets.ModelViewSet):
    queryset = Clip.objects.all()
    serializer_class = ClipSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description']