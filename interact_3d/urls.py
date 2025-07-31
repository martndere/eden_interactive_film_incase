from django.urls import path
from . import views

app_name = 'interact_3d'

urlpatterns = [
    # This maps the URL /interact/viewer/ to our new view
    path('viewer/', views.model_viewer_view, name='model_viewer'),
]

