from django.db import models

# Create your models here.


class Categories(models.Model):
    id = models.TextField(primary_key=True)
    parent_id = models.TextField(default=None, blank=True, verbose_name='Категория',
                                  null=True)
    name_category = models.CharField(max_length=255, verbose_name='Название категории')

    create_utc = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        db_table = 'categories'


class PasswordStores(models.Model):
    id = models.TextField(primary_key=True)
    login = models.TextField(verbose_name='Логин')
    password = models.TextField(verbose_name='Пароль')
    description = models.TextField(blank=True, verbose_name='Описание')
    create_utc = models.TextField(blank=True, verbose_name='Время создания')
    parent_id = models.TextField(verbose_name='Категория')

    class Meta:
        db_table = 'password_store'