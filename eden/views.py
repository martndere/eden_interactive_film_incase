from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Clip, Choice

def home(request):
    return render(request, 'eden/home.html')

def clip_a_view(request):
    # Load Clip A using its name (case-insensitive match)
    clip = Clip.objects.filter(name__icontains="Clip A").first()
    choices = clip.choices.all() if clip else []
    return render(request, 'eden/clip_a.html', {'clip': clip, 'choices': choices})

def clip_detail(request, slug):
    # Replace dashes with underscores to enforce underscore naming
    template_slug = slug.replace('-', '_')
    clip = get_object_or_404(Clip, slug=slug)
    choices = clip.choices.all()
    return render(request, f'eden/{template_slug}.html', {'clip': clip, 'choices': choices})

def branch_view(request, character):
    # This view may become obsolete as branching is now data-driven
    mapping = {
        'ralph': 'clip-c',   # Ralph → Clip C
        'taika': 'clip-f',   # Taika → Clip F
        'tpma': 'clip-q',    # TPMA → Clip Q
    }
    slug = mapping.get(character)
    if not slug:
        return HttpResponse("Unknown character", status=404)
    
    return redirect('clip_detail', slug=slug)
