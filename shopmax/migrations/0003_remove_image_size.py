# Generated by Django 5.0.2 on 2024-03-07 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shopmax", "0002_alter_size_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="image",
            name="size",
        ),
    ]
