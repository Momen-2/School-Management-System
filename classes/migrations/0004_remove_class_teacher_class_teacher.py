# Generated by Django 4.2.2 on 2023-08-01 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0012_remove_teacher_test_field"),
        ("classes", "0003_remove_class_teacher_class_teacher"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="class",
            name="teacher",
        ),
        migrations.AddField(
            model_name="class",
            name="teacher",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.teacher",
            ),
            preserve_default=False,
        ),
    ]
