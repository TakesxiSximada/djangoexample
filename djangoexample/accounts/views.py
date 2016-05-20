from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class AccountViewSet(ModelViewSet):
    serializer_class = serializers.AccountSerializer
    queryset = models.Account.objects.all()
