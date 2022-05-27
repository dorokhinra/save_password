from django.contrib import admin

from .models import *
# Register your models here.


class PasswordStoreAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'password', 'description', 'time_create')
    list_display_links = ('id', 'login')


admin.site.register(PasswordStore, PasswordStoreAdmin)


class IndexContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    list_display_links = ('id', 'content')


admin.site.register(IndexContent, IndexContentAdmin)


class KeyStorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'user')
    list_display_links = ('id', 'key')


admin.site.register(KeyStorage, KeyStorageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_category', 'time_create')
    list_display_links = ('name_category', )
    search_fields = ('name_category', )


admin.site.register(Category, CategoryAdmin)