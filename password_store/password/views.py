import os
import uuid
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, FileResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
import json, asyncio

from django.utils.decorators import classonlymethod
from django.views import View
from django.views.generic import ListView, CreateView
from django.views.generic.edit import DeleteView, UpdateView
from password.forms import AddCategoryForm, AddElement, LoginUserForm, AddEncryptKey, AddUserKey, AddUserForm
from password.utils import DataMixim, DecryptMixim, SyncDiscMixin, EncryptMixin, RegisterUserMailMixin
# Create your views here.
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
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
        del c_def['bar']
        return dict(list(context.items()) + list(list(c_def.items())))


# def index(requests):
#     bar = ['Синхронизация', 'Шифрование']
#     return render(requests, 'password/index.html', {'menu': menu, 'bar': bar})


class LoginUser(DataMixim, LoginView):
    """
    Представления для авторизации пользователя
    """
    form_class = LoginUserForm
    template_name = 'password/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        del c_def['bar']
        return dict(list(context.items()) + list(list(c_def.items())))

    def get_success_url(self):
        return reverse_lazy('home')


# Выход пользователя
def logout_user(request):
    logout(request)
    return redirect('login')


class DeleteElement(DeleteView):
    """
    Удаление элемента со страницы pass_reestr
    """
    model = PasswordStore
    success_url = reverse_lazy('pass_reestr', kwargs={'parent_id': 0})


class PassReestr(DataMixim, ListView):
    """
    Изменение и просмотр елементов (логин пароль и т.д)
    Обновление элемента с помощью класса UpdateElem
    """
    model = PasswordStore
    template_name = 'password/pass_reestr.html'
    context_object_name = 'pass_table'
    form_class = AddElement

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['parent_id']
        if pk != '0':
            cat_name = Category.objects.get(pk=pk)
            cat_name = cat_name.name_category
        else:
            cat_name = 'Родитель'
        c_def = self.get_user_context(title='Реестр элементов', cats=[],
                                      form=self.form_class, cat_name=cat_name, user_id=self.request.user.id)
        return dict(list(context.items()) + list(list(c_def.items())))

    # Отображение определенных элементов
    def get_queryset(self):
        return PasswordStore.objects.filter(parent_id=self.kwargs['parent_id'], user_id=self.request.user.id)


class UpdateElem(EncryptMixin, TemplateView):
    """
    Обновление элемента на странице pass_reestr
    """
    model = PasswordStore
    success_url = reverse_lazy('pass_reestr', kwargs={'parent_id': 0})

    def post(self, request, *args, **kwargs):
        data = self.request.POST#
        key = self.check_key_an_token(self.request.user.id, data['keyPass'])
        elem = self.model.objects.get(pk=kwargs['pk'])
        elem.login = self.encrypt_message(key['msg'], data['login']).decode()
        elem.password = self.encrypt_message(key['msg'], data['password']).decode()
        elem.description = self.encrypt_message(key['msg'], data['description']).decode()
        elem.save()
        return HttpResponseRedirect(reverse_lazy('pass_reestr', kwargs={'parent_id': elem.parent_id_id}))


class DecryptElem(DecryptMixim, EncryptMixin,  TemplateView):
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        key = self.check_key_an_token(self.request.user.id, self.request.POST['key'])
        if key['status'] == 'err':
            return key['msg']
        decrypt_elem = self.decryption(elem_id=self.kwargs['pk'], key=key['msg'])
        data = {'pk': decrypt_elem.pk,
                'login': decrypt_elem.login,
                'password': decrypt_elem.password,
                'description': decrypt_elem.description}
        return HttpResponse(json.dumps({'data': data}), content_type='application/json')


# async def post(request, *args, **kwargs):
#     tes = SyncDiscMixin()
#     if request.POST:
#         if kwargs['ts'] == 'ya_disk':
#             token = request.POST['token']
#             msg = await tes.check_token(token)
#         else:
#             code = request.POST['code']
#             msg = await tes.check_code(code)
#         return msg
#
#
# async def main_func(request, *args, **kwargs):
#     msg = await asyncio.gather(post(request, *args, **kwargs))
#     return HttpResponse(json.dumps({'data': msg[0]}), content_type='application/json')


class SyncDisc(DataMixim, SyncDiscMixin, TemplateView):
    template_name = 'password/setting_pass_ya_disk.html'

    @classonlymethod  # Чтобы выполнять асинхронные операции в классе, сначала необходимо переопределить метод as_view()
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        data_items = self.get_user_context(title='Синхронизация')
        return dict(list(context.items()) + list(list(data_items.items())))

    async def get(self, request, *args, **kwargs):
        if self.kwargs.get('ts', False) and self.kwargs['ts'] == 'file':
            data_items = self.get_user_file(file='ff')
            return FileResponse(open(data_items['file'], 'rb'))

        return self.render_to_response(self.get_context_data(**kwargs))

    async def post(self, request, *args, **kwargs):
        if self.request.POST:
            if self.kwargs['ts'] == 'ya_disk':
                token = self.request.POST['token']
                msg = await self.check_token(token)
            else:
                code = self.request.POST['code']
                msg = await self.check_code(code)
            return HttpResponse(json.dumps({'data': msg}), content_type='application/json')


# class TestAsync(SyncDiscMixin, TemplateView):
#     @classonlymethod
#     def as_view(cls, **initkwargs):
#         view = super().as_view(**initkwargs)
#         view._is_coroutine = asyncio.coroutines._is_coroutine
#         return view
#
#     async def post(self, request, *args, **kwargs):
#         if self.request.POST:
#             if self.kwargs['ts'] == 'ya_disk':
#                 token = self.request.POST['token']
#                 msg = await self.check_token(token)
#             else:
#                 code = self.request.POST['code']
#                 msg = await self.check_code(code)
#             return HttpResponse(json.dumps({'data': msg}), content_type='application/json')


class EditReestr(DataMixim, EncryptMixin, TemplateView):
    """
    Класс для создание и удаления категорий и для создания элементов для этих категорий
    """
    form_class = AddCategoryForm
    elem_form = AddElement
    template_name = 'password/edit_reestr.html'
    success_url = reverse_lazy('home')

    #  Изменение контекста прилождения, если необходимо добавить свои значения и переменные
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Изменение элементов', cats=[], form=self.form_class,
                                      add_ell_form=self.elem_form, user_id=self.request.user.id)
        # if self.request.GET:
        #     print(self.request.GET['data'])
        return dict(list(context.items()) + list(list(c_def.items())))

    def post(self, request, *args, **kwargs):
        dict_result = dict(self.request.POST)
        self.result = {}
        for i in dict_result:
            self.result[i] = dict_result[i][0]
        self.result['user_id'] = self.request.user.id
        if not self.request.POST.get('name_category', False):
            return self.create_elem()
        else:
            return self.create_category(**kwargs)

    def create_elem(self):
        key = self.check_key_an_token(self.request.user.id, self.result['key_pass'])
        if key['status'] == 'err':
            return key['msg']
        for i in self.result:
            if i not in ['csrfmiddlewaretoken', 'key_pass', 'user_id', 'parent_id']:
                self.result[i] = self.encrypt_message(key['msg'], self.result[i]).decode()
        category_form = self.elem_form(self.result)
        try:
            category_form.save()
            category_form.clean()
            return HttpResponse(json.dumps({'msg': "<p>Элемент добавлен</p>"}), content_type='application/json')
        except:
            return HttpResponse(json.dumps({'msg': '<p>Что-то пошло не так!</p>'}), content_type="application/json")

    def create_category(self, **kwargs):
        category_form = self.form_class(self.result)
        try:
            category_form.save()
            category_form.clean()
            context = self.get_context_data(**kwargs)
            c_def = self.get_user_context(cats=[], user_id=self.request.user.id)
            return HttpResponse(json.dumps({'msg': "<p>Категория добавлена</p>",
                                            'tree': dict(list(list(c_def.items())))}), content_type="application/json")
        except:
            return HttpResponse(json.dumps({'msg': "<p>Поробуйте выбрать другую категорию, возможна эта удалена!</p>",
                                            'tree': ''}), content_type="application/json")


class DeleteCategory(DataMixim, DeleteView):
    """
    Удаление категории на странице edit_reestr
    """
    model = Category
    success_url = reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        pk = kwargs['pk']
        del_cats = Category.objects.get(pk=pk)
        del_cats.delete()
        cats = Category.objects.filter(user_id=self.request.user.id).values('id', 'name_category', 'parent_id')
        initTree = self.import_data(cats)
        return HttpResponse(json.dumps({'msg': "<p>Категория удалена!</p>",
                                        'tree': {'cats': initTree}}))


# Шифрование элементов Здесь создается ключ для шифрования
class EncryptView(EncryptMixin, DataMixim, TemplateView):
    form_class = AddEncryptKey
    template_name = 'password/encryption.html'
    path_key = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        msg = self.check_exist_key(self.request.user.id)
        form_class_file = AddUserKey(initial={'user': self.request.user.id})
        # self.form_class_file.fields['user'].value = self.request.user.id
        data_items = self.get_user_context(title='Шифрование', form=self.form_class,
                                           msg=msg, form_file=form_class_file)
        return dict(list(context.items()) + list(list(data_items.items())))

    def post(self, request, *args, **kwargs):
        if self.request.POST:
            self.path_key = os.path.normpath(
                os.path.join(self.path, f"{self.request.user.id}.key"))  # Создаем ключ и сохраняем его в файл

            msg = self.create_key(self.request.user.id, self.request.POST['password'], self.path_key)
            return HttpResponse(json.dumps(msg), content_type='application/json')


class DownloadUserKey(CreateView):
    form_class = AddUserKey
    success_url = reverse_lazy('encryption')
    login_url = reverse_lazy('login')
    # def post(self, request, *args, **kwargs):
    #     p=1
    #     return HttpResponse(1)


class DeleteUserKey(DeleteView):
    model = KeyStorage
    success_url = reverse_lazy('encryption')


class RegisterUser(DataMixim, RegisterUserMailMixin, CreateView):
    form_class = AddUserForm
    template_name = 'password/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        del c_def['bar']
        return dict(list(context.items()) + list(list(c_def.items())))

    def post(self, request, *args, **kwargs):
        reg_token = uuid.uuid4()
        form = self.form_class(self.request.POST)
        if form.is_valid():
            self.set_user_data(self.request.POST, str(reg_token))
            self.send_mail(reg_token, self.request.POST['email'])
            return render(request, 'password/register_timer.html')
        # form = self.form_class(json.loads(response))
        # if form.is_valid():
        #     form.save()
        #     return redirect('login')
        return super().post(request, *args, **kwargs)


class AcceptRegister(DataMixim, RegisterUserMailMixin, TemplateView):
    template_name = 'password/accept_register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        check_reg = self.check_reg_id(kwargs['reg_id'])
        if check_reg['status']:
            form = AddUserForm(check_reg['msg'])
            form.save()
            data_items = self.get_user_context(title='Успешная регистрация', status='ok')
        else:
            data_items = self.get_user_context(title='Регистрация не пройдена!', status='err')
        del data_items['bar']
        return dict(list(context.items()) + list(list(data_items.items())))



# Create your views here.
@receiver(pre_delete, sender=KeyStorage)  #  Отслеживает изменение с путм к файлу и если в БД путь удаляется удаляется и сам ФАЙЛ
def image_model_delete(sender, instance, **kwargs):
    if instance.key.name:
        instance.key.delete(False)

