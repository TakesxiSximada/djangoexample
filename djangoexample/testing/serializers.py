from rest_framework.serializers import (
    ModelSerializer,
)


from . import models


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'


class ThumbnailSerializer(ModelSerializer):
    class Meta:
        model = models.Thumbnail
        fields = '__all__'
