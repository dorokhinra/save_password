# Generated by Django 4.0.4 on 2022-06-04 21:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('password', '0005_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.UUID('7a192865-406f-43d4-9bc4-6e653b90cc9f'), primary_key=True, serialize=False, unique=True),
        ),
    ]
