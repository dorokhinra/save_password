import os
from collections import deque

from password.models import *
import yadisk_async
import datetime

class DataMixim:
    # paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        if context.get('cats', False) != False:
            cats = Category.objects.all().values('id', 'name_category', 'parent_id')
            context['cats'] = self.import_data(cats)

        return context
    # region функция
    @staticmethod
    def import_data(data, root=''): #Построение деоева элементов
        list_data = []
        if root == '':
            root = list_data  # Вначале создаем пустой список
            root.append({'id': '0', 'text': 'Родитель', 'icon': "fa fa-folder", 'href': ''})
        seen = {}
        values = deque(data) # Загоняем данные в много этереируемую запоминаемую коллекцию
        while values:
            value = values.popleft()
            if value['parent_id'] == None:
                parent = root   # Если это родитель оставляем все как есть
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
            data_item = {'id':value['id'], 'text': value['name_category'], 'icon': "fa fa-folder", 'href': ''} # f'/edit_reestr/{value["id"]}'
            parent.append(data_item)
            seen[dbid] = parent[len(parent) - 1]

        return root
    # endregion


class DecryptMixim:

    def decryption(self, **kwargs):
        elem_id = kwargs['elem_id']
        enc_data = PasswordStore.objects.get(pk=elem_id)
        return enc_data


class SyncDiscMixin:
    app_path = os.path.abspath(os.getcwd())
    path_db = os.path.normpath(os.path.join(app_path, "db.sqlite3"))
    y = yadisk_async.YaDisk("e4b953a1900241a99dad6416dc0c0218", "a74315e22a73436683986016c1ae7c57")

    def get_user_context(self, **kwargs):
        context = kwargs
        if context.get('file', False):
            context['file'] = self.path_db
        else:
            bar = [{'name': 'Синхронизация', 'url': 'setting_pass'},
                   {'name': 'Шифрование', 'url': 'encryption'}]
            context['bar'] = bar
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