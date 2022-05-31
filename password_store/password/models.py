from django.conf import settings
from django.db import models

# Create your models here.


def file_path(instance, filename):
    return '{}.key'.format(instance.user.id)


class IndexContent(models.Model):
    content = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Описание для главной страници'
        verbose_name_plural = 'Описание для главной страници'


class KeyStorage(models.Model):
    key = models.FileField(upload_to=file_path, verbose_name='Ключи пользователя')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Ключи пользователей'
        verbose_name_plural = 'Ключи пользователей'


class Category(models.Model):
    parent_id = models.ForeignKey('self', default=None, blank=True, on_delete=models.CASCADE,  verbose_name='Категория',
                                  null=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    name_category = models.CharField(max_length=255, verbose_name='Название категории')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                verbose_name='Пользователь', default=None)

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = 'Название категории'
        verbose_name_plural = 'Название категории'
        ordering = ['-time_create', 'name_category']


class PasswordStore(models.Model):
    login = models.TextField(verbose_name='Логин')
    password = models.TextField(verbose_name='Пароль')
    description = models.TextField(blank=True, verbose_name='Описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    parent_id = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория',
                                    related_name='get_category')
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                verbose_name='Пользователь', default=None)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Элементы авторизации'
        verbose_name_plural = 'Элементы авторизации'
        ordering = ['-time_create']