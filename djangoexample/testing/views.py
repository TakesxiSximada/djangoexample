from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class ArticleViewSet(ModelViewSet):
    serializer_class = serializers.ArticleSerializer
    queryset = models.Article.objects.all()


class ThumbnailViewSet(ModelViewSet):
    serializer_class = serializers.ThumbnailSerializer
    queryset = models.Thumbnail.objects.all()
