from django.db.models import (
    Model,
    CharField,
    DateTimeField,
)
from django.contrib.auth.models import (
    AbstractUser,
)


class User(AbstractUser):
    unique_name = CharField(max_length=124, default='', unique=True)
    display_name = CharField(max_length=124, default='')
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    deleted_at = DateTimeField(blank=True, null=True)
