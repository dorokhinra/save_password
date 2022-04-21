from django.shortcuts import render

from django.views.generic import ListView
from password.utils import DataMixim
# Create your views here.

# @login_required(redirect_field_name='login')
from password.models import *
# Класс отображения всех элементов согласно модели на странице (отвечает ListView)
from password.utils import DataMixim



class PassHome(DataMixim, ListView):
    model = IndexContent
    template_name = 'password/index.html'
    context_object_name = 'content'# свой шаблон необходимо указать в этой переменной


    # Изменение контекста прилождения, если необходимо добавить свои значения и переменные
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(list(c_def.items())))

# def index(requests):
#     bar = ['Синхронизация', 'Шифрование']
#     return render(requests, 'password/index.html', {'menu': menu, 'bar': bar})

def login(request):
    return render(request, 'password/login.html')

def pass_reestr(request):
    return render(request, 'password/pass_reestr.html')

def setting_pass(request):
    bar = ['Синхронизация', 'Шифрование']
    return render(request, 'password/setting_pass.html', {'bar': bar})

def edit_reestr(request):
    return render(request, 'password/edit_reestr.html')

# Create your views here.
