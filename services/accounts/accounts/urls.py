from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='accounts',
        default_version='v1',
        description='accounts service doc',
        terms_of_service='No',
        contact=openapi.Contact(email='isenandreev@gmail.com'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/v1/accounts/admin/', admin.site.urls),
    path('api/v1/accounts/', include('api.urls')),

    # Swagger doc
    path(
        'api/v1/accounts/swagger/',
        schema_view.with_ui(
            'swagger',
            cache_timeout=0
        ),
        name='schema-swagger-ui'
    ),
    path(
        'api/v1/accounts/redoc/',
        schema_view.with_ui(
            'redoc',
            cache_timeout=0
        ),
        name='schema-redoc'
    ),
]

urlpatterns += static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
)
