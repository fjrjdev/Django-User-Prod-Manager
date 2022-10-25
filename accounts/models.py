from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Account(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    username = models.CharField(max_length=200, unique=True)

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    is_seller = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['id']

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        ]
