from rest_framework.serializers import (
    ModelSerializer,
)


from . import models


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = models.Organization
        fields = ('display_name',)
        read_only_fields = ('unique_name',)
