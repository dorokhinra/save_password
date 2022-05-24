from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import *


class AddCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parent_id'].empty_label = "Категория не выбрана"
        self.fields['name_category'].label = 'Наименование категории'

    class Meta:
        model = Category
        fields = ['parent_id', 'name_category']
        widgets = {
            'name_category': forms.TextInput(attrs={'class': 'form-control'})
        }


class AddElement(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].label = 'Описание'

    class Meta:
        model = PasswordStore
        fields = ['parent_id', 'login', 'password', 'description']
        widgets = {
            'login': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Пароль', 'type': 'password'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'})
        }


class LoginUserForm(AuthenticationForm):

    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Введите логин для авторизации'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control', 'placeholder': 'Введите пароль для авторизации', 'type': 'password'}))
