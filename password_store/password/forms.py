from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import *


# Форма для добавления категории
class AddCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent_id'].empty_label = "Категория не выбрана"
        self.fields['name_category'].label = 'Наименование категории'

    class Meta:
        model = Category
        fields = ['parent_id', 'name_category', 'user_id']
        widgets = {
            'name_category': forms.TextInput(attrs={'class': 'form-control'})
        }


# Форма для добавления эелементов
class AddElement(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].label = 'Описание'

    # Класс для отображежния дополнительного функционала
    class Meta:
        model = PasswordStore
        fields = ['parent_id', 'login', 'password', 'description', 'user_id']  # Отображаемые поля в форме
        widgets = {
            'login': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Пароль', 'type': 'password'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


# Кастомизированнная форма для авторизации
class LoginUserForm(AuthenticationForm):

    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Введите логин для авторизации'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control', 'placeholder': 'Введите пароль для авторизации', 'type': 'password'}))


# Форма для ввода пароля для ключа
class AddEncryptKey(forms.Form):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
                                   'class': 'form-control', 'type': 'password'}))


class AddUserKey(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['key'].label = 'Загрузка ключа для пользователя'

    class Meta:
        model = KeyStorage
        fields = ['key', 'user']  # Отображаемые поля в форме
        widgets = {
            'key': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Выберите файл для загрузки'}),
            'user': forms.HiddenInput()
        }


class AddUserForm(UserCreationForm):
    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Введите логин'}))
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control', 'placeholder': 'Введите пароль',
                                    'type': 'password'}))
    password2 = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control', 'placeholder': 'Повторите ввод пароля',
                                   'type': 'password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Адрес эелектронно почты', 'required': 'required'}),
        }