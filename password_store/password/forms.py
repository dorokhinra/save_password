from django import forms
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

    class Meta:
        model = password_store
        fields = ['parent_id', 'login', 'password', 'description']
        widgets = {

        }
