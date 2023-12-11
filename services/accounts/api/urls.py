from django.urls import include, path

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
        'auth/',
        include('djoser.social.urls')
    ),
]
