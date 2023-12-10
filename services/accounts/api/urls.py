from django.urls import include, path

from . import views


urlpatterns = [
    path('', include('djoser.urls')),
    path('users/me/', views.UserMeView.as_view()),
    path(
        'auth/',
        include('djoser.social.urls')
    ),
]
