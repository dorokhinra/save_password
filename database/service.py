from collections import deque

from PyQt5.QtSql import QSqlQuery
from qt_core import *
from database.query import query_data


class StandartItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(255, 255, 255), data_text=None):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        # self.setEnabled(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)
        self.setData(data_text, Qt.UserRole)


class CatigoriesView:
    def __init__(self, parent, session):
        self.parent = parent
        self.session = session
        self.treeModel = QStandardItemModel()
        self.rootNode = self.treeModel.invisibleRootItem()
        self.parent.treeView_2.setHeaderHidden(True)
        self.parent.treeView_2.setModel(self.treeModel)
        self.parent.treeView_2.setAnimated(True)


    def get_data(self, auth):
        self.session.open(auth['login'], auth['password'])
        self.query = QSqlQuery(self.session)
        query_string = query_data()['query_all_categories']
        self.query.prepare(query_string)
        self.query.exec_()
        list_categories = []
        while self.query.next():
            id = self.query.value(0)
            parent_id = self.query.value(1)
            name_category = self.query.value(2)
            create_utc = self.query.value(3)
            list_categories.append({'id': id, 'parent_id': parent_id, 'name_category': name_category, 'create_utc': create_utc})
        # self.sort_cat(list_categories, 0, elem_list=[])
        self.import_data(list_categories)
        self.parent.treeView_2.expandAll()

    def import_data(self, data, root=''):
        self.treeModel.setRowCount(0)
        if root is '':
            root = self.treeModel.invisibleRootItem()
            root.appendRow(StandartItem('Родительский элемент'))
        seen = {}
        values = deque(data)
        while values:
            value = values.popleft()
            if value['parent_id'] == '':
                parent = root
            else:
                pid = value['parent_id']
                if pid not in seen:
                    values.append(value)
                    continue
                parent = seen[pid]
            dbid = value['id']
            data_item = StandartItem(value['name_category'], data_text=value['id'])
            parent.appendRow([
                data_item
            ])
            seen[dbid] = parent.child(parent.rowCount() - 1)



class CreateElement():
    def __init__(self):
        pass

