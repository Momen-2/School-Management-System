# Generated by Django 4.2.2 on 2023-08-01 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("classes", "0006_class_teacher"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="class",
            name="teacher",
        ),
    ]