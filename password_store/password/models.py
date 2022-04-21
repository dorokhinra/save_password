from django.db import models


# Create your models here.
class IndexContent(models.Model):
    content = models.TextField(blank=True)


class Category(models.Model):
    parent_id = models.ForeignKey('self', default=None, on_delete=models.CASCADE, verbose_name='Категория')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    name_category = models.CharField(max_length=255, verbose_name='Название категории')

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = 'Название категории'
        verbose_name_plural = 'Название категории'
        ordering = ['-time_create', 'name_category']


class password_store(models.Model):
    login = models.CharField(max_length=255, verbose_name='Логин')
    password = models.CharField(max_length=255, verbose_name='Пароль')
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    parent_id = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория',
                                    related_name='get_category')

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Данные для автоизации'
        verbose_name_plural = 'Данные для автоизации'
        ordering = ['-time_create']