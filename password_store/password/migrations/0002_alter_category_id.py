# Generated by Django 4.0.4 on 2022-06-04 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('password', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.TextField(default='<function uuid4 at 0x00000192F5B0E950>', editable=False, primary_key=True, serialize=False),
        ),
    ]