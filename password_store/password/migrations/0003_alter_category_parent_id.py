# Generated by Django 4.0.4 on 2022-05-05 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('password', '0002_alter_category_parent_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='password.category', verbose_name='Категория'),
        ),
    ]
