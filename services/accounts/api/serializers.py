from rest_framework import serializers, permissions
from rest_framework.authtoken.models import Token

from predictions.models import Predict
from predictions.services import start_predicting
from users.models import User


class UserGETSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'first_name',
            'last_name',
        )
        read_only_fields = fields


class PredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Predict
        fields = (
            'id',
            'status',
            'predict',
        )
        read_only_fields = fields

    def create(self, validated_data):
        request = self.context.get('request')
        predict = super().create(validated_data)
        key = Token.objects.get(user=request.user).key

        predicting_response = start_predicting(
            predict.id,
            key
        )

        if predicting_response.status_code != 200:
            response_data = str(predicting_response.json())

            raise serializers.ValidationError(
                f'Error response from predict service. {response_data}',
            )

        return predict


class InsertPredictSerializer(serializers.ModelSerializer):
    permission_classes = (permissions.AllowAny,)

    class Meta:
        model = Predict
        fields = (
            'id',
            'status',
            'predict',
        )
        read_only_fields = (
            'id',
            'status'
        )
