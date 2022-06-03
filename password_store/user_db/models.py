from django.db import models

# Create your models here.


class Categories(models.Model):
    parent = models.ForeignKey('self', default=None, blank=True, on_delete=models.CASCADE, verbose_name='Категория',
                                  null=True)
    create_utc = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    name_category = models.CharField(max_length=255, verbose_name='Название категории')

    class Meta:
        db_table = 'categories'


class PasswordStores(models.Model):
    login = models.TextField(verbose_name='Логин')
    password = models.TextField(verbose_name='Пароль')
    description = models.TextField(blank=True, verbose_name='Описание')
    create_utc = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    parent = models.ForeignKey('Categories', on_delete=models.CASCADE, verbose_name='Категория',
                                  related_name='get_category')

    class Meta:
        db_table = 'password_store'