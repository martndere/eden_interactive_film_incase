from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clip-a/', views.clip_a_view, name='clip_a'),
    path('branch/<str:character>/', views.branch_view, name='branch_view'),
    path('<slug:slug>/', views.clip_detail, name='clip_detail'),
]
