from django.urls import path
from django.contrib.auth import views as auth_views  # <-- Add this line
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('my-films/', views.UserFilmListView.as_view(), name='my_films'),
    path('film/create/', views.UserFilmCreateView.as_view(), name='film_create'),
    path('film/<int:pk>/', views.UserFilmDetailView.as_view(), name='film_detail'),
    path('clip/create/<int:film_id>/', views.UserClipCreateView.as_view(), name='clip_create'),
    path('choice/create/<int:clip_id>/', views.UserChoiceCreateView.as_view(), name='choice_create'),
    path('clip/<int:pk>/edit/', views.edit_clip, name='edit_clip'),
]
