from rest_framework import serializers

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
