from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('films/', views.UserFilmListView.as_view(), name='my_films'),
    path('films/create/', views.UserFilmCreateView.as_view(), name='film_create'),
    path('films/<int:pk>/', views.UserFilmDetailView.as_view(), name='film_detail'),
    path('films/<int:film_id>/clip/create/', views.UserClipCreateView.as_view(), name='clip_create'),
    path('clip/<int:pk>/edit/', views.edit_clip, name='clip_edit'),
    path('clip/<int:clip_id>/choice/create/', views.UserChoiceCreateView.as_view(), name='choice_create'),
    path('profile/', views.profile, name='profile'),
]