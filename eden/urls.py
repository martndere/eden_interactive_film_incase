from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .views import ClipViewSet, upload_clip, delete_clip

# Create DRF router for Clip API ViewSet
router = DefaultRouter()
router.register(r'api/clips', ClipViewSet, basename='clip')

urlpatterns = [
    # =========================
    # Frontend / page views
    # =========================
    path('', views.home, name='home'),
    path('clip-a/', views.clip_a_view, name='clip_a'),
    path('branch/<str:character>/', views.branch_view, name='branch_view'),
    path('<slug:slug>/', views.clip_detail, name='clip_detail'),

    # =========================
    # HTMX partials
    # =========================
    path('api/clips/html/', views.clip_list_partial, name='clip_list_partial'),

    # =========================
    # Upload + delete clips (secured)
    # =========================
    path('api/clips/upload/', upload_clip, name='upload_clip'),
    path('api/clips/delete/<int:clip_id>/', delete_clip, name='delete_clip'),

    # =========================
    # JWT token auth
    # =========================
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # =========================
    # API routes from router (clips list, detail)
    # =========================
    path('', include(router.urls)),
]
