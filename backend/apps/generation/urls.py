from django.urls import path
from . import views

app_name = 'generation'

urlpatterns = [
    path('generate-image/', views.generate_image_view, name='generate_image'),
]