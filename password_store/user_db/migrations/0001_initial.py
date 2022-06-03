# Generated by Django 4.0.5 on 2022-06-03 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_utc', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('name_category', models.CharField(max_length=255, verbose_name='Название категории')),
                ('parent_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='user_db.categories', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='PasswordStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.TextField(verbose_name='Логин')),
                ('password', models.TextField(verbose_name='Пароль')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('create_utc', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('parent_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_category', to='user_db.categories', verbose_name='Категория')),
            ],
        ),
    ]
