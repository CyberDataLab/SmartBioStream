# Generated by Django 4.2.11 on 2025-03-24 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="address",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="birth_date",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="city",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="country",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="creation_date",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="gender",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="postal_code",
        ),
    ]
