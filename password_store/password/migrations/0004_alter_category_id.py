# Generated by Django 4.0.4 on 2022-06-04 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password', '0003_alter_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.TextField(default='55e592a2-600e-49df-8f03-cb5757abc1df', primary_key=True, serialize=False, unique=True),
        ),
    ]
