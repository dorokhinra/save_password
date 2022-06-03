import json
import os
from collections import deque

import redis
from django.http import HttpResponse
from django.core.mail import EmailMessage, EmailMultiAlternatives
from password.forms import AddUserKey
from password.models import *
import yadisk_async
import datetime
from django.template.loader import render_to_string
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

from user_db.models import Categories


class DataMixim:
    # paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        if context.get('cats', False) != False:
            cats = Category.objects.filter(user_id=context['user_id']) \
                .values('id', 'name_category', 'parent_id')
            context['cats'] = self.import_data(cats)
        else:
            bar = [{'name': 'Синхронизация', 'url': 'setting_pass'},
                   {'name': 'Шифрование', 'url': 'encryption'}]
            context['bar'] = bar
        return context

    # region функция
    @staticmethod
    def import_data(data, root=''):  # Построение деоева элементов
        list_data = []
        if root == '':
            root = list_data  # Вначале создаем пустой список
            root.append({'id': '0', 'text': 'Родитель', 'icon': "fa fa-folder", 'href': ''})
        seen = {}
        values = deque(data)  # Загоняем данные в много этереируемую запоминаемую коллекцию
        while values:
            value = values.popleft()
            if value['parent_id'] == None:
                parent = root  # Если это родитель оставляем все как есть
            else:
                pid = value['parent_id']
                if pid not in seen:
                    values.append(value)
                    continue
                p = seen[pid]
                if p.get('nodes', False) == False:
                    p['nodes'] = []
                parent = p['nodes']
            dbid = value['id']
            data_item = {'id': value['id'], 'text': value['name_category'], 'icon': "fa fa-folder",
                         'href': ''}  # f'/edit_reestr/{value["id"]}'
            parent.append(data_item)
            seen[dbid] = parent[len(parent) - 1]

        return root
    # endregion


class DecryptMixim:

    def decryption(self, **kwargs):
        elem_id, key = kwargs['elem_id'], kwargs['key']
        enc_data = PasswordStore.objects.get(pk=elem_id)
        f = Fernet(key)
        enc_data.login = f.decrypt(enc_data.login.encode()).decode()
        enc_data.password = f.decrypt(enc_data.password.encode()).decode()
        enc_data.description = f.decrypt(enc_data.description.encode()).decode()

        return enc_data


class SyncDiscMixin:
    app_path = os.path.abspath(os.getcwd())
    path_db = os.path.normpath(os.path.join(app_path, "db.sqlite3"))
    y = yadisk_async.YaDisk("e4b953a1900241a99dad6416dc0c0218", "a74315e22a73436683986016c1ae7c57")


    def get_user_file(self, **kwargs):
        context = kwargs
        if context.get('file', False):
            # user_id = context['user_id']
            # cats = Category.objects.filter(user_id=user_id).values('name_category', 'parent_id')
            # password_store = PasswordStore.objects.filter(user_id=user_id).values('login', 'password',
            #                                                                       'description', 'parent_id')
            #
            # for name_category, parent_id in cats:
            #     Categories.objects.create(name_category=name_category, parent_id=parent_id)
            # for login, password, escription, parent_id in password_store:
            #     pass

            context['file'] = self.path_db
        return context

    async def check_token(self, token):
        if token == '':
            return {'msg': self.y.get_code_url(), 'status': 'url'}
        else:
            self.y.token = token
            if await self.y.check_token():
                return await self.save_ya_disk()

    async def check_code(self, code):
        try:
            response = await self.y.get_token(code)
            self.y.token = response.access_token
            if await self.y.check_token():
                return {'msg': response.access_token, 'status': 'token'}
        except yadisk_async.exceptions.BadRequestError:
            return {'msg': '', 'status': 'error'}

    async def save_ya_disk(self):
        try:
            dir_name = await self.check_YaDisk_file_and_dir()
            if dir_name['dirname'] == '':
                await self.y.mkdir("disk:/Приложения/store")
            # print(datetime.datetime.now())
            await self.y.upload(self.path_db, f"disk:/Приложения/store/{datetime.datetime.now()}")
            return {'msg': 'Сохранено на яндекс диск!', 'status': 'ok'}
        except yadisk_async.exceptions.ForbiddenError:
            return {'msg': 'Что-то пошло не так!', 'status': 'error'}

    async def check_YaDisk_file_and_dir(self):
        store_async = await self.y.listdir('disk:/Приложения/')
        dir_name = ''
        list_file = []
        async for name in store_async:
            if name['name'] == 'store':
                dir_name = name['name']
                list_file = await self.y.listdir('disk:/Приложения/store/')
                list_file = sorted([dict_file_name['name'] async for dict_file_name in list_file])

        return {'dirname': dir_name, 'list_file': list_file}


class EncryptMixin:
    app_path = os.path.abspath(os.getcwd())
    folder = "media"
    path = os.path.join(app_path, folder)

    def create_key(self, user_id, user_key, path_key):
        key_path_db = KeyStorage.objects.filter(user=user_id)
        if not key_path_db:
            key_pass = Fernet.generate_key()
            f = self.generate_enc_token(user_key)
            token = f.encrypt(key_pass)
            KeyStorage.objects.create(user_id=user_id, key='{}.key'.format(user_id))
            try:
                with open(path_key, 'wb') as key_file:
                    key_file.write(token)
                    key_file.close()
                return {'msg': 'Ключ успешно создан!', 'passKey': user_key, 'status': 'ok'}
            except:
                return {'msg': 'Ошибка!', 'passKey': user_key, 'status': 'error'}
        else:
            try:
                self.check_key_pass(user_key, path_key)
                return {'passKey': user_key, 'status': 'ok'}
            except:
                return {'msg': 'Ошибка не верный пароль!', 'passKey': user_key, 'status': 'error'}

    def check_key_pass(self, user_key, path_key):
        f = self.generate_enc_token(user_key)
        with open(path_key, 'rb') as file:
            encrypt_key = file.read()
        try:
            self.key = f.decrypt(encrypt_key)
        except:
            raise ValueError

    def check_exist_key(self, user_id):
        key_path_db = KeyStorage.objects.filter(user=user_id)
        if key_path_db:
            return {'msg': 'Ключ существует введите пароль для работы!', 'key_id': key_path_db[0].id}
        else:
            return {'msg': 'Ключ не существует введите пароль для создания или загрузите свой!', 'key_id': ''}

    def generate_enc_token(self, user_key):
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=b"staticsalt", iterations=100000,
                         backend=default_backend())
        key = base64.urlsafe_b64encode(kdf.derive(user_key.encode()))
        return Fernet(key)

    def check_key_an_token(self, user_id, key_pass):
        path_key = os.path.normpath(
            os.path.join(self.path, f"{user_id}.key"))
        key = self.decrypt_key(key_pass, path_key)
        if not key:
            return {'msg': HttpResponse(json.dumps({'msg': '<p>Что-то пошло не так!</p>'}),
                                        content_type="application/json"), 'status': 'err'}
        return {'msg': key, 'status': 'ok'}

    @staticmethod
    def encrypt_message(key, message):
        f = Fernet(key)
        return f.encrypt(message.encode())

    def decrypt_key(self, key, path_key):
        f = self.generate_enc_token(key)

        with open(path_key, 'rb') as file:
            encrypt_key = file.read()
        try:
            return f.decrypt(encrypt_key)
        except:
            return False

class RegisterUserMailMixin:
    redis_instance = redis.StrictRedis(password=settings.REDIS_PASS, host=settings.REDIS_HOST,
                                       port=settings.REDIS_PORT, db=0)
    # smtpObj = smtplib.SMTP('smtp.yandex.ru', 465)

    def set_user_data(self, data, reg_token):
        dict_result = dict(data)
        result = {}
        for i in dict_result:
            result[i] = dict_result[i][0]
        self.redis_instance.set(reg_token, json.dumps(result), ex=235)


    def send_mail(self, reg_id, email):
        html_content = render_to_string('password/accept_register_smtp.html', {'reg_id': str(reg_id)})
        email_msg = EmailMultiAlternatives('Подтверждение регистрации', 'Text',  to=[str(email)])
        email_msg.attach_alternative(html_content, "text/html")
        email_msg.send()

    def check_reg_id(self, reg_id):
        value = self.redis_instance.get(str(reg_id))
        if value:
            data = json.loads(value)
            return {'status': True, 'msg': data}
        return {'status': False}

