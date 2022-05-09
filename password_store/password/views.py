from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.urls import reverse_lazy
import json
from django.views import View
from django.views.generic import ListView, CreateView
from django.views.generic.edit import DeleteView
from password.forms import AddCategoryForm, AddElement
from password.utils import DataMixim
# Create your views here.
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
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
    elem_form = AddElement
    template_name = 'password/edit_reestr.html'

    success_url = reverse_lazy('home')

    #  Изменение контекста прилождения, если необходимо добавить свои значения и переменные
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Изменение элементов', cats=[], form=self.form_class,
                                      add_ell_form=self.elem_form)
        # if self.request.GET:
        #     print(self.request.GET['data'])
        return dict(list(context.items()) + list(list(c_def.items())))

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('name_category', False) == False:
            return self.create_elem()
        else:
            return self.create_category(**kwargs)

    def create_elem(self):
        category_form = self.elem_form(self.request.POST)
        try:
            category_form.save()
            category_form.clean()
            return HttpResponse(json.dumps({'msg': "<p>Элемент добавлен</p>"}), content_type='application/json')
        except:
            return HttpResponse(json.dumps({'msg': '<p>Что-то пошло не так!</p>'}), content_type="application/json")

    def create_category(self, **kwargs):
        category_form = self.form_class(self.request.POST)
        try:
            category_form.save()
            category_form.clean()
            context = self.get_context_data(**kwargs)
            c_def = self.get_user_context(cats=[])
            return HttpResponse(json.dumps({'msg': "<p>Категория добавлена</p>",
                                            'tree': dict(list(list(c_def.items())))}), content_type="application/json")
        except:
            return HttpResponse(json.dumps({'msg': "<p>Поробуйте выбрать другую категорию, возможна эта удалена!</p>",
                                            'tree': ''}), content_type="application/json")


class DeleteCategory(DeleteView):
    model = Category
    template_name = 'password/confirm_delete.html'
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        del_cats = Category.objects.get(pk=pk)
        del_cats.delete()
        cats = Category.objects.all().values('id', 'name_category', 'parent_id')
        initTree = DataMixim().import_data(cats)
        return HttpResponse(json.dumps({'msg': "<p>Категория удалена!</p>",
                                        'tree': {'cats': initTree}}))


# class DeleteCat(DeleteView):
#     model = Category
#
#     @csrf_exempt
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         p = self.get_queryset()
#         print(request)
#         return HttpResponse('')


# @csrf_exempt
# def delete_category(request):
#
#     if request.method == 'DELETE':
#         p = request.body.decode()
#         cat_id = Category.objects.get(pk=p)
#         cat_id.delete()
#         cats = Category.objects.all().values('id', 'name_category', 'parent_id')
#         initTree = DataMixim().import_data(cats)
#     return HttpResponse(json.dumps({'msg': "<p>Категория удалена!</p>",
#                                    'tree': {'cats': initTree}}))


def encryption(request):
    bar = [{'name': 'Синхронизация', 'url': 'setting_pass'}, {'name': 'Шифрование', 'url': 'encryption'}]
    return render(request, 'password/encryption.html', {'bar': bar, 'title': 'Шифрование'})

# Create your views here.
