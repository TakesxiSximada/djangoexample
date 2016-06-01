from django.db import models


class Article(models.Model):
    id = models.BigIntegerField(primary_key=True)


class Thumbnail(models.Model):
    class Meta:
        unique_together = (
            ('article', 'size')
        )
    id = models.BigIntegerField(primary_key=True)
    article = models.ForeignKey(Article)
    size = models.CharField(default='large')
