from collections import deque

from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery
from qt_core import *
from database.query import query_data, query_insert_cat, query_insert_elem


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
    def __init__(self, parent, session, model):
        self.parent = parent
        self.session = session
        self.treeModel = model
        # self.treeModel = QStandardItemModel()
        # self.rootNode = self.treeModel.invisibleRootItem()
        # self.parent.treeView_2.setHeaderHidden(True)
        # self.parent.treeView_2.setModel(self.treeModel)
        # self.parent.treeView_2.setAnimated(True)


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


class CatigoriesViewForReestr:

    def __init__(self, parent, session):
        self.parent = parent
        self.session = session
        self.treeModel = QStandardItemModel()
        self.rootNode = self.treeModel.invisibleRootItem()
        self.parent.treeView.setHeaderHidden(True)
        self.parent.treeView.setModel(self.treeModel)
        self.parent.treeView.setAnimated(True)



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
        self.parent.treeView.expandAll()

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


class CreateCategory():
    def __init__(self, parent, session, id, model):
        self.parent = parent
        self.session = session
        self.id = id
        self.treeModel = model

    def create_cat(self):
        if self.parent.edit_name_category.text() != '':
            if self.id == None:
                self.id = ''
            data = {'parent_id': self.id, 'name': self.parent.edit_name_category.text()}
            query_string = query_insert_cat(data)
            self.session.open( self.parent.db_login_edit.text(), self.parent.db_pass_edit.text())
            self.query = QSqlQuery(self.session)
            self.query.prepare(query_string)
            self.query.exec_()
            set_cat = CatigoriesView(self.parent, self.session, self.treeModel)
            set_cat.get_data({'login': self.parent.db_login_edit.text(), 'password': self.parent.db_pass_edit.text()})
            self.parent.label_success_info.setVisible(False)
            self.clear_all()
        else:
            self.parent.info_for_edit_elements.setText('Укажите наименование категории!')
            self.parent.label_success_info.setVisible(False)

    def create_elem(self):
        if self.parent.edit_login.text() != '' and self.parent.edit_password.text():
            if self.id is None or self.id == '':
                self.parent.info_for_edit_elements.setText('Сначала выберите родительский элемент!')
            else:
                data = {'login': self.parent.edit_login.text(),
                        'password': self.parent.edit_password.text(),
                        'description': self.parent.description_edit.toPlainText(),
                        'parent_id': self.id}
                query_string = query_insert_elem(data)
                self.session.open(self.parent.db_login_edit.text(), self.parent.db_pass_edit.text())
                self.query = QSqlQuery(self.session)
                self.query.prepare(query_string)
                self.query.exec_()
                set_cat = CatigoriesView(self.parent, self.session, self.treeModel)
                set_cat.get_data(
                    {'login': self.parent.db_login_edit.text(), 'password': self.parent.db_pass_edit.text()})
                self.parent.label_success_info.setVisible(True)
                self.parent.label_success_info.setText('Данные успешно добалены!')
                self.clear_all()
        else:
            self.parent.info_for_edit_elements.setText('Заполните логин и пароль!')
            self.parent.label_success_info.setVisible(False)

    def clear_all(self):
        self.parent.edit_login.setText('')
        self.parent.edit_password.setText('')
        self.parent.description_edit.setText('')
        self.parent.edit_name_category.setText('')
        self.parent.info_for_edit_elements.setText('')


class Table_view():
    def __init__(self, parent, session, parent_id):
        self.parent = parent
        self.session = session
        self.parent_id = parent_id
        self.set_date_in_table()
        self.create_table_view_data()

    def set_date_in_table(self):
        self.model = QtSql.QSqlTableModel(self.parent, self.session)
        self.model.setTable('password_store')
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, "Id")
        self.model.setHeaderData(1, Qt.Horizontal, "Логин")
        self.model.setHeaderData(2, Qt.Horizontal, "Пароль")
        self.model.setHeaderData(3, Qt.Horizontal, "описание")
        self.model.setHeaderData(4, Qt.Horizontal, "время создания")
        self.model.setHeaderData(5, Qt.Horizontal, "Категория")
        self.model.setFilter(f"parent_id LIKE '%{self.parent_id}%'")
        self.model.select()

    def create_table_view_data(self):
        self.parent.ui.tableView.setModel(self.model)
        self.parent.ui.tableView.verticalHeader().setDefaultSectionSize(35)
        self.parent.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.parent.ui.tableView.setColumnWidth(1, 200)
        self.parent.ui.tableView.setColumnWidth(2, 200)
        self.parent.ui.tableView.setColumnWidth(3, 240)
        self.parent.ui.tableView.hideColumn(0)
        self.parent.ui.tableView.hideColumn(4)
        self.parent.ui.tableView.hideColumn(5)




