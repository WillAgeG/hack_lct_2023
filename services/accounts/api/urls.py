from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(
    'predictions',
    views.PredictViewSet,
    basename='predicts'
)

router.register(
    'insert_predictions',
    views.InsertPredictViewSet,
    basename='predicts'
)

urlpatterns = [
    path('', include(router.urls)),
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
