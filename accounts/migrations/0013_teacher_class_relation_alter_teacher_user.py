# Generated by Django 4.2.2 on 2023-08-01 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("classes", "0005_remove_class_teacher"),
        ("accounts", "0012_remove_teacher_test_field"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="class_relation",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="classes.class",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="teacher",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
