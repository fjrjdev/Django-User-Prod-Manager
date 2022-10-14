from django.db import models
from django.contrib.auth.models import AbstractUser
from traitlets import default


class Partner(AbstractUser):
    name = models.CharField(max_length=200, unique=True)
    cnpj = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=200, unique=True)

    description = models.TextField(default='Not Defined', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = [
        "name",
        "email",
    ]
