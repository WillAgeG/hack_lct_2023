from django.urls import include, path

from . import views


urlpatterns = [
    path(
        '',
        include('djoser.urls')
    ),
    path(
        '',
        include('djoser.urls.authtoken')
    ),
    path(
        '',
        include('social_django.urls', namespace='social')
    ),
    path(
        'users/google/token/',
        views.UserGoogleTokenView.as_view()
    ),
    path(
        'auth/',
        include('djoser.social.urls')
    ),
]
