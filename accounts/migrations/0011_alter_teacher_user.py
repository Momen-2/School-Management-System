# Generated by Django 4.2.2 on 2023-08-01 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0010_teacher"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="teacher",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]