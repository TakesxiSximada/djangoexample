from django.db.models import (
    Model,
    DateTimeField,
)


class Account(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
