# Generated by Django 2.2.24 on 2021-07-15 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_customtext_homepage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customtext",
            name="title",
        ),
        migrations.AddField(
            model_name="customtext",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="customtext",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customtext",
            name="name",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="customtext",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=30, null=True
            ),
        ),
        migrations.AddField(
            model_name="customtext",
            name="updated_at",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
