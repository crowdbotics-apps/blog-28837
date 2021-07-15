from django.conf import settings
from django.db import models


class HomePage(models.Model):
    "Generated Model"
    body = models.TextField()


class CustomText(models.Model):
    "Generated Model"
    description = models.TextField(
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=20,
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=30,
        decimal_places=2,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True,
    )
