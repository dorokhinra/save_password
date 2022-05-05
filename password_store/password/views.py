from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView

from password.forms import AddCategoryForm
from password.utils import DataMixim
# Create your views here.
from django.views.generic import TemplateView

# @login_required(redirect_field_name='login')
from password.models import *
# Класс отображения всех элементов согласно модели на странице (отвечает ListView)
from password.utils import DataMixim


class PassHome(DataMixim, ListView):
    model = IndexContent
    template_name = 'password/index.html'
    context_object_name = 'content'  # свой шаблон необходимо указать в этой переменной

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


def setting_pass_ya_disk(request):
    bar = [{'name':'Синхронизация', 'url': 'setting_pass'}, {'name': 'Шифрование', 'url': 'encryption'}]
    return render(request, 'password/setting_pass_ya_disk.html', {'bar': bar, 'title': 'Синхронизация'})


class EditReestr(DataMixim, TemplateView):
    form_class = AddCategoryForm
    template_name = 'password/edit_reestr.html'

    success_url = reverse_lazy('home')

    #  Изменение контекста прилождения, если необходимо добавить свои значения и переменные
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Изменение элементов', cats=[], form=self.form_class)
        # if self.request.GET:
        #     print(self.request.GET['data'])
        return dict(list(context.items()) + list(list(c_def.items())))

    def post(self, request, *args, **kwargs):
        category_form = self.form_class(self.request.POST)
        category_form.save()
        context = self.get_context_data(**kwargs)

        print(123)
        return self.render_to_response(context)

def encryption(request):
    bar = [{'name': 'Синхронизация', 'url': 'setting_pass'}, {'name': 'Шифрование', 'url': 'encryption'}]
    return render(request, 'password/encryption.html', {'bar': bar, 'title': 'Шифрование'})

# Create your views here.
