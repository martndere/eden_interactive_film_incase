# Core Django
from django.shortcuts import render, get_object_or_404, redirect
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
    """
    Finds the designated starting clip and redirects to its detail page.
    Falls back to the first clip created if none is designated.
    """
    start_clip = Clip.objects.filter(is_start_clip=True).first()
    if not start_clip:
        start_clip = Clip.objects.order_by('created_at').first()
    
    if not start_clip:
        return render(request, 'eden/no_clips.html') # A fallback page
        
    return redirect('eden:clip_detail', slug=start_clip.slug)

def clip_detail(request, slug):
    clip = get_object_or_404(Clip, slug=slug)
    choices = clip.choices.all()
    context = {'clip': clip, 'choices': choices}

    # If the request is from HTMX, render only the partial.
    # Otherwise, render the full page.
    if request.htmx:
        return render(request, 'eden/partials/clip_content.html', context)
    
    return render(request, 'eden/clip_detail.html', context)

def clip_list_partial(request):
    q = request.GET.get('q', '')
    clips = Clip.objects.all()  # (You could filter by q if needed)
    return render(request, 'eden/partials/clip_list_partial.html', {'clips': clips})

# ----------------------------
# API views
# ----------------------------

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAdminUser])
def upload_clip(request):
    name = request.data.get('name')
    description = request.data.get('description', '')
    video_file = request.FILES.get('video_file')

    if not name or not video_file:
        return Response({'error': 'Name and video_file are required'}, status=400)

    clip = Clip.objects.create(
        name=name,
        description=description,
        slug=slugify(name),
        video=video_file
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
    permission_classes = [IsAuthenticatedOrReadOnly] # Allows anyone to read, but only auth'd to write
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']
    lookup_field = 'slug' # Use slug instead of pk in URL for detail views