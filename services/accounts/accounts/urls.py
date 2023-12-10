from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api/v1/accounts/admin/', admin.site.urls),
    path('api/v1/accounts/', include('allauth.urls')),
    path('api/v1/accounts/', include('allauth.socialaccount.urls')),
]

urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
