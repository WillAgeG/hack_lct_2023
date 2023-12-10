from django.urls import include, path

# from . import views


urlpatterns = [
    path('accounts/', include('djoser.urls')),
    path(
        'accounts/auth/',
        include('djoser.social.urls')
    ),
    path('accounts/token/', include('djoser.urls.authtoken')),
]
