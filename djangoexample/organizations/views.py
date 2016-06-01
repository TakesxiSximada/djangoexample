from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class OrganizationViewSet(ModelViewSet):
    serializer_class = serializers.OrganizationSerializer
    queryset = models.Organization.objects.all()
