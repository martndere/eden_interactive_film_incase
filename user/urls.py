from django.urls import path
from . import views

app_name = 'user_content'

urlpatterns = [
    path('my-films/', views.UserFilmListView.as_view(), name='my_films'),
    path('film/create/', views.UserFilmCreateView.as_view(), name='film_create'),
    path('film/<int:pk>/', views.UserFilmDetailView.as_view(), name='film_detail'),
    path('clip/create/<int:film_id>/', views.UserClipCreateView.as_view(), name='clip_create'),
    path('choice/create/<int:clip_id>/', views.UserChoiceCreateView.as_view(), name='choice_create'),
]