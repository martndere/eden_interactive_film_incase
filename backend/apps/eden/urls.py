from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

app_name = 'eden'

# API Router
router = DefaultRouter()
router.register(r'clips', views.ClipViewSet, basename='clip')

# Grouping API patterns for clarity and to be included under a single prefix
api_urlpatterns = [
    # Router URLs for /api/clips/, /api/clips/<pk>/ etc.
    path('', include(router.urls)),

    # HTMX partials
    path('clips/html/', views.clip_list_partial, name='clip_list_partial'),

    # Custom actions on clips
    path('clips/upload/', views.upload_clip, name='upload_clip'),
    path('clips/delete/<int:clip_id>/', views.delete_clip, name='delete_clip'),

    # Auth
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns = [
    # Page/frontend views
    path('', views.home, name='home'),

    # Include all API endpoints under the /api/ prefix
    path('api/', include(api_urlpatterns)),
    
    # This generic slug pattern MUST come last.
    path('<slug:slug>/', views.clip_detail, name='clip_detail'),
]