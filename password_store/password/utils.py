import os
from collections import deque

from password.models import *


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

    def get_user_context(self, **kwargs):
        context = kwargs
        if context.get('file', False):
            app_path = os.path.abspath(os.getcwd())
            path_db = os.path.normpath(os.path.join(app_path, "db.sqlite3"))
            context['file'] = path_db
        else:
            bar = [{'name': 'Синхронизация', 'url': 'setting_pass'},
                   {'name': 'Шифрование', 'url': 'encryption'}]
            context['bar'] = bar
        return context