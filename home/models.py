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
        null=True,
        blank=True,
        max_length=20,
    )
    price = models.DecimalField(
        null=True,
        blank=True,
        max_digits=30,
        decimal_places=2,
    )
    created_at = models.DateTimeField(
        null=True,
        blank=True,
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        null=True,
        blank=True,
        auto_now=True,
    )


class App(models.Model):
    "Generated Model"
    name = models.CharField(
        max_length=50,
    )
    description = models.TextField()
    type = models.CharField(
        max_length=20,
    )
    framework = models.CharField(
        max_length=20,
    )
    domain_name = models.CharField(
        max_length=50,
    )
    screenshot = models.URLField()
    subscription = models.IntegerField()
    user = models.IntegerField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )


class Subscription(models.Model):
    "Generated Model"
    user = models.IntegerField(
        "home.App",
    )
    plan = models.IntegerField()
    app = models.IntegerField()
    active = models.BooleanField()
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
