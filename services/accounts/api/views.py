import logging

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from social_django.utils import load_strategy

from predictions.models import Predict
from .serializers import PredictSerializer, InsertPredictSerializer

logger = logging.getLogger(__name__)


class UserGoogleTokenView(APIView):
    @swagger_auto_schema(
        responses={status.HTTP_200_OK: openapi.Schema(
            title="UserGoogleTokenView",
            type=openapi.TYPE_OBJECT,
            properties={
                'access_token': openapi.Schema(type=openapi.TYPE_STRING),
                'refresh_token': openapi.Schema(type=openapi.TYPE_STRING)
            }
        )}
    )
    def get(self, request):
        try:
            social = request.user.social_auth.get(provider='google-oauth2')

            # Обновляем токены
            strategy = load_strategy(request=request)
            social.refresh_token(strategy)

            data = {
                'access_token': social.extra_data['access_token'],
                'refresh_token': social.extra_data.get('refresh_token'),
                'credentials': social.extra_data
            }

            return Response(data=data, status=status.HTTP_200_OK)

        except Exception as e:
            logger.error('Cannot get google access, refresh tokens. %s', e)
            return Response(
                data={'message': 'Error occurred while fetching tokens'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class PredictViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.ListModelMixin,
                     GenericViewSet):
    serializer_class = PredictSerializer

    def get_queryset(self):
        return Predict.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class InsertPredictViewSet(mixins.UpdateModelMixin,
                           GenericViewSet):
    serializer_class = InsertPredictSerializer

    def get_queryset(self):
        return Predict.objects.filter(
            user=self.request.user
        )
