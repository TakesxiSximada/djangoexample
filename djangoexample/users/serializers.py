from rest_framework.serializers import (
    ModelSerializer,
)


from . import models


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = ('display_name',)
        read_only_fields = ('unique_name',)
