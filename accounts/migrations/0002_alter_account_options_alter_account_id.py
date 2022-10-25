# Generated by Django 4.1.2 on 2022-10-21 20:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="account",
            options={"ordering": ["id"]},
        ),
        migrations.AlterField(
            model_name="account",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
    ]
