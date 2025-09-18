from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # Add Django's built-in auth views (for login, logout, password management)
    # This makes views available at URLs like /accounts/login/, /accounts/logout/, etc.
    path('accounts/', include('django.contrib.auth.urls')),
    # API endpoints
    # path('api/generation/', include('apps.generation.urls')), # Commented out until the app is created
    # Include other app URLs. The 'eden' app contains both web and API routes.
    path('generation/', include('apps.generation.urls')),
    path('', include('apps.eden.urls')),
    path('users/', include('apps.user.urls')),
    path('interact-3d/', include('apps.interact_3d.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)