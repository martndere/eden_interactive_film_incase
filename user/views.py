from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import UserFilm, UserClip, UserChoice

class UserFilmListView(LoginRequiredMixin, ListView):
    model = UserFilm
    template_name = 'user_content/my_films.html'
    context_object_name = 'films'

    def get_queryset(self):
        return UserFilm.objects.filter(user=self.request.user)

class UserFilmCreateView(LoginRequiredMixin, CreateView):
    model = UserFilm
    fields = ['title', 'description', 'is_public']
    template_name = 'user_content/film_form.html'
    success_url = reverse_lazy('user_content:my_films')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UserFilmDetailView(LoginRequiredMixin, DetailView):
    model = UserFilm
    template_name = 'user_content/film_detail.html'
    context_object_name = 'film'

class UserClipCreateView(LoginRequiredMixin, CreateView):
    model = UserClip
    fields = ['name', 'video', 'thumbnail', 'narrative', 'prompt_time', 'audio_prompt', 'order']
    template_name = 'user_content/clip_form.html'

    def form_valid(self, form):
        form.instance.film_id = self.kwargs['film_id']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user_content:film_detail', kwargs={'pk': self.kwargs['film_id']})

class UserChoiceCreateView(LoginRequiredMixin, CreateView):
    model = UserChoice
    fields = ['to_clip', 'label', 'order']
    template_name = 'user_content/choice_form.html'

    def form_valid(self, form):
        form.instance.from_clip_id = self.kwargs['clip_id']
        return super().form_valid(form)

    def get_success_url(self):
        clip = UserClip.objects.get(pk=self.kwargs['clip_id'])
        return reverse_lazy('user_content:film_detail', kwargs={'pk': clip.film_id})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'user_content/register.html', {'form': form})

@login_required
def edit_clip(request, pk):
    clip = get_object_or_404(UserClip, pk=pk, film__user=request.user)
    if request.method == 'POST':
        # Handle form submission for edits (e.g., start/end times)
        clip.edit_start = request.POST.get('edit_start')
        clip.edit_end = request.POST.get('edit_end')
        # Save other edits as needed
        clip.save()
        return redirect('user_content:film_detail', pk=clip.film_id)
    return render(request, 'user_content/edit_clip.html', {'clip': clip})