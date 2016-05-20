from rest_framework.serializers import (
    ModelSerializer,
)


from . import models


class AccountSerializer(ModelSerializer):
    class Meta:
        model = models.Account
        fields = '__all__'
