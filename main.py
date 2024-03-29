#IMPORT MUDULES
import asyncio
import os
import glob
import sys
import time
#IMPORT QTQORE
from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery

from database.query import query_delete_category, query_change_category_on_double_click, query_delete_element_in_cat, \
    query_delet_elem, query_update_elem
from qt_core import *
# UI
from gui.windows.ui_main_ui import Ui_MainWindow

#SETTING_UI
from gui.widgets.setup_ui import SettingsUi

#БаЗа Данных
from database.session import DbSession

from database.service import CatigoriesView, CreateCategory, CatigoriesViewForReestr, Table_view
from system_modules.decript_elem import decrypt_elem

from system_modules.synchronization import CheckSync

#Import py_context_menu
from gui.widgets.py_context_menu import ContextMenuOn, ContextMenuForTableElem

from  system_modules.encryption import Encryption

#MAIN_WINDOW
class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
#########Настройки приложения
        path = os.path.abspath(os.getcwd())
        path_ini = os.path.normpath(os.path.join(path, "settings.ini"))
        self.settings = QSettings(path_ini, QSettings.IniFormat)
        self.path_html = os.path.normpath(os.path.join(path, "html"))
        self.template1 = os.path.normpath(os.path.join(self.path_html, "info1.html"))
        self.template2 = os.path.normpath(os.path.join(self.path_html, "info2.html"))
        self.template3 = os.path.normpath(os.path.join(self.path_html, "info3.html"))
        self.template4 = os.path.normpath(os.path.join(self.path_html, "info4.html"))
        self.template_ya1 = os.path.normpath(os.path.join(self.path_html, "infoYa1.html"))
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        SettingsUi(self.ui, app)

        self.ui.roll_up_btn.clicked.connect(self.on_min)
        self.ui.exit_btn.clicked.connect(self.closeEvent)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        self.ui.btn_settings.clicked.connect(self.show_settings)
        self.ui.btn_pass_reestr.clicked.connect(self.show_reestr)
        self.id = ''

        self.ui.frame_element_edit.setVisible(False)
        # self.ui.edit_name_category.text()


        #получение название элемента при нажатии на элемент в деревена странице редактирования
        self.ui.treeView_2.clicked.connect(self.get_value_category)

        self.ui.btn_edit_pass_reestr.clicked.connect(self.show_edit_reestr)
        #установка первой страницей синхронизации с базой данных
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4)
        # Проверка токена
        self.sync_disk = CheckSync(self.settings, self.ui, self.style_sheet_info())
        self.sync_disk.check_sync()
        self.ui.input_code_btn.clicked.connect(self.sync_disk.input_code)

        self.ui.get_code_btn.clicked.connect(self.sync_disk.get_token)

        # Сохранение на Ядиск БД
        self.ui.btn_push.clicked.connect(self.save_disk) # save_disk

        #Загрузка на локальный диск
        self.ui.btn_update.clicked.connect(self.upload_disk)

        self.ui.cotegori_radio.clicked.connect(self.show_category_edit)

        self.ui.elemen_radio.clicked.connect(self.show_element_edit)

        self.ui.confitm_edit_reestr_btn.clicked.connect(self.confirm_edit)

        #Кнопки переключения для страници с настройками
        self.ui.main_menu_btn_set.clicked.connect(self.go_to_back)
        self.ui.git_btn.clicked.connect(self.show_git_settings)
        self.ui.key_btn.clicked.connect(self.show_key_settings)
        self.ui.db_btn.clicked.connect(self.show_db_settings)
        self.setTreeModel()
        #Кнопки на странице изменения реестра
        self.ui.main_menu_page_edit_btn.clicked.connect(self.go_to_back)

        #Кнопка переключения главного меню для реестра
        self.ui.go_back_menu_reestr.clicked.connect(self.go_to_back)

        self.ui.confirm_edit_elem_btn.clicked.connect(self.edit_element_in_pass_reestr)

        #получение parent_id по нажатию на элемент
        self.ui.treeView.clicked.connect(self.select_category_for_select_element)

        self.ui.delete_elem_btn.clicked.connect(self.del_elem)

        self.db = ''
        #БАЗА дАННЫХ
        self.check_db()
        self.ui.pushButton.clicked.connect(self.create_db)
        self.check_os_type()
        # Показать выпадающее меню при клике мыши
        self.context_menu = ContextMenuOn(self.del_widget)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.treeView_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.treeView_2.customContextMenuRequested.connect(self.context_menu.on_custom_context_menu)
        # Контекстное меню на таблицу с паролями
        self.context_menu_for_table_pass = ContextMenuForTableElem(self.decrypt_elem)
        self.ui.tableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tableView.customContextMenuRequested.connect(self.context_menu_for_table_pass.on_custom_context_menu)

        #Шифрование
        self.encrypt = Encryption(self.ui)
        self.encrypt.check_key()

        self.ui.btn_add_key.clicked.connect(self.confirm_edit_key)

        #расшифрованный элемент
        self.data_decrypt_elem = {}
        self.show()


    def confirm_edit_key(self):
        self.encrypt.bush_connect_button()
        if self.ui.db_login_edit.text() != '' and self.ui.db_pass_edit.text() != '':
            if self.encrypt.key != '':
                self.ui.btn_pass_reestr.setEnabled(True)
                self.ui.btn_pass_reestr.setToolTip('')
                self.ui.btn_edit_pass_reestr.setEnabled(True)
                self.ui.btn_edit_pass_reestr.setToolTip('')

    def edit_element_in_pass_reestr(self):
        if self.data_decrypt_elem != {}:

            if self.ui.decrypt_login_edit.text() != '' and self.ui.decrypt_pass_edit.text() != '':
                data = {'id': self.data_decrypt_elem['id'],
                        'login':  self.encrypt.encrypt_message(self.ui.decrypt_login_edit.text()).decode(),
                        'password':  self.encrypt.encrypt_message(self.ui.decrypt_pass_edit.text()).decode(),
                        'description':  self.encrypt.encrypt_message(self.ui.decrypt_description_edit.toPlainText()).decode()}
                self.db.session.open(self.ui.db_login_edit.text(), self.ui.db_pass_edit.text())
                self.query = QSqlQuery(self.db.session)
                query_string_elem = query_update_elem(data)
                self.query.prepare(query_string_elem)
                self.query.exec_()
                self.clear_widget_vis_pass_reestr()
                Table_view(self, self.db.session, self.data_decrypt_elem['parent_id'])
                self.data_decrypt_elem = {}

            else:
                self.ui.label_info_pass_reestr.setText('Заполните логин и пароль!')
        else:
            pass

    def clear_widget_vis_pass_reestr(self):
        self.ui.decrypt_login_edit.setText('')
        self.ui.decrypt_pass_edit.setText('')
        self.ui.decrypt_description_edit.setText('')
        self.ui.label_info_pass_reestr.setText('')

    def del_elem(self):
        if self.data_decrypt_elem != {}:
            self.db.session.open(self.ui.db_login_edit.text(), self.ui.db_pass_edit.text())
            self.query = QSqlQuery(self.db.session)
            query_string_elem = query_delet_elem(self.data_decrypt_elem['id'])
            self.query.prepare(query_string_elem)
            self.query.exec_()
            self.clear_widget_vis_pass_reestr()
            Table_view(self, self.db.session, self.data_decrypt_elem['parent_id'])
            self.data_decrypt_elem = {}
        else:
            pass

    def decrypt_elem(self, wid, index):
        row = index.row()
        index = self.ui.tableView.model().index(row, 0)
        elem_id = self.ui.tableView.model().data(index)
        auth = {'login': self.ui.db_login_edit.text(), 'password': self.ui.db_pass_edit.text()}
        self.data_decrypt_elem = decrypt_elem(auth=auth, session=self.db.session, id=elem_id, decrypt_func=self.encrypt.decrypt_message)
        self.ui.decrypt_login_edit.setText(self.data_decrypt_elem['login'])
        self.ui.decrypt_pass_edit.setText(self.data_decrypt_elem['password'])
        self.ui.decrypt_description_edit.setText(self.data_decrypt_elem['description'])

    def setTreeModel(self):
        self.treeModel = QStandardItemModel()
        self.rootNode = self.treeModel.invisibleRootItem()
        self.ui.treeView_2.setHeaderHidden(True)
        self.ui.treeView_2.setModel(self.treeModel)
        self.ui.treeView_2.setAnimated(True)
        self.treeModel.dataChanged.connect(self.change_category_on_double_click)

    def change_category_on_double_click(self, val):
        cat_id = val.data(Qt.UserRole)
        cat_data = val.data()
        query_string = query_change_category_on_double_click(cat_id, cat_data)
        self.db.session.open(self.ui.db_login_edit.text(), self.ui.db_pass_edit.text())
        self.query = QSqlQuery(self.db.session)
        self.query.prepare(query_string)
        self.query.exec_()
        self.ui.treeView_2.update()
        self.ui.element_name.setText(cat_data)


    def select_category_for_select_element(self, val):
        self.ui.label_16.setText(val.data())
        Table_view(self, self.db.session, val.data(Qt.UserRole))
        self.clear_widget_vis_pass_reestr()
        self.data_decrypt_elem = {}
        # print(val.data(Qt.UserRole))

    def del_widget(self, id):
        query_string = query_delete_category(id)
        self.db.session.open(self.ui.db_login_edit.text(), self.ui.db_pass_edit.text())
        self.query = QSqlQuery(self.db.session)
        self.query.prepare(query_string)
        self.query.exec_()
        query_string_elem = query_delete_element_in_cat(id)
        self.query.prepare(query_string_elem)
        self.query.exec_()
        set_cat = CatigoriesView(self.ui, self.db.session, self.treeModel)
        set_cat.get_data(
            {'login': self.ui.db_login_edit.text(), 'password': self.ui.db_pass_edit.text()})
        self.id = ''
        self.ui.element_name.setText('Родительский элемент')


    def get_value_category(self, val):
        self.id = val.data(Qt.UserRole)
        self.ui.element_name.setText(val.data())

    def upload_disk(self):
        self.sync_disk.update_db_to_Ya_disk()
        self.animation_info(self.ui.info_ya_api)

    def check_db(self):
        app_path = os.path.abspath(os.getcwd())
        folder = "database/db_file"
        path = os.path.join(app_path, folder)
        path_db = os.path.normpath(os.path.join(path, "password_store.sqlite"))
        if os.path.exists(path_db):
            self.ui.radioButton_2.setChecked(True)
            if self.ui.db_login_edit.text() != '' and self.ui.db_pass_edit.text() != '':
                self.db = DbSession()
                self.db.create_table(self.db.session, self.ui.db_login_edit.text(), self.ui.db_pass_edit.text())
                self.ui.pushButton.setEnabled(False)
                self.ui.db_pass_info.setStyleSheet(self.style_sheet_info()['success'])
                self.ui.db_pass_info.setSource(QtCore.QUrl.fromLocalFile(self.template3))
                self.animation_info(self.ui.db_pass_info)
                if self.encrypt.key != '':
                    self.ui.btn_pass_reestr.setEnabled(True)
                    self.ui.btn_pass_reestr.setToolTip('')
                    self.ui.btn_edit_pass_reestr.setEnabled(True)
                    self.ui.btn_edit_pass_reestr.setToolTip('')
            else:
                self.ui.btn_pass_reestr.setEnabled(False)
                self.ui.btn_pass_reestr.setToolTip(
                    'Для разблокирования кнопки\n необходимо настроить подключение к БД!')
                self.ui.btn_edit_pass_reestr.setEnabled(False)
                self.ui.btn_edit_pass_reestr.setToolTip('Для разблокирования кнопки\n необходимо настроить подключение к БД!')
                self.ui.db_pass_info.setStyleSheet(self.style_sheet_info()['danger'])
                self.ui.db_pass_info.setSource(QtCore.QUrl.fromLocalFile(self.template1))
        else:
            self.ui.btn_pass_reestr.setEnabled(False)
            self.ui.btn_edit_pass_reestr.setEnabled(False)
            self.ui.db_pass_info.setStyleSheet(self.style_sheet_info()['danger'])
            self.ui.db_pass_info.setSource(QtCore.QUrl.fromLocalFile(self.template2))
            # self.animation_info(self.ui.db_pass_info)

    def confirm_edit(self):
        create = CreateCategory(self.ui, self.db.session, self.id, self.treeModel)
        if self.ui.cotegori_radio.isChecked():
            create.create_cat()
        else:
            create.create_elem(self.encrypt.encrypt_message)



    def create_db(self):
        if self.ui.db_login_edit.text() != '' and self.ui.db_pass_edit.text() != '':
            if self.ui.radioButton.isChecked():
                self.db = DbSession()
                self.db.create_table(self.db.session, self.ui.db_login_edit.text(), self.ui.db_pass_edit.text())
                self.ui.label_info_db.setText("")
                self.ui.pushButton.setEnabled(False)
                self.ui.db_pass_info.setStyleSheet(self.style_sheet_info()['success'])
                self.ui.db_pass_info.setSource(QtCore.QUrl.fromLocalFile(self.template3))
                self.animation_info(self.ui.db_pass_info)
            elif self.ui.radioButton_2.isChecked():
                self.check_db()
        else:
            self.ui.db_pass_info.setStyleSheet(self.style_sheet_info()['danger'])
            self.ui.db_pass_info.setSource(QtCore.QUrl.fromLocalFile(self.template4))
            self.animation_info(self.ui.db_pass_info)

    def save_disk(self):
        self.sync_disk.save_disk()
        self.animation_info(self.ui.info_ya_api)

    def show_db_settings(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_6)
        self.animation_info(self.ui.db_pass_info)

    def show_git_settings(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4)
        self.animation_info(self.ui.info_ya_api)

    def show_key_settings(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_5)
        self.animation_info(self.ui.textEdit)

    def show_settings(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        self.animation_info(self.ui.info_ya_api)

    def show_reestr(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        set_cat = CatigoriesViewForReestr(self.ui, self.db.session)
        set_cat.get_data({'login': self.ui.db_login_edit.text(), 'password': self.ui.db_pass_edit.text()})
        self.clear_widget_vis_pass_reestr()
        self.data_decrypt_elem = {}
        self.ui.tableView.update()

    def go_to_back(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)

    def show_edit_reestr(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_edit)
        set_cat = CatigoriesView(self.ui, self.db.session, self.treeModel)
        set_cat.get_data({'login': self.ui.db_login_edit.text(), 'password': self.ui.db_pass_edit.text()})

    @staticmethod
    def style_sheet_info():

        info_success = """
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(91, 193, 200, 1), stop:1 rgba(91, 193, 200, 0));
        border: none;
        border-radius: 25px;
        padding: 5px;
        padding-top: 20px;
        """
        info_error = """
          background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(228, 17, 55, 1), stop:1 rgba(228, 17, 55, 0));
        border: none;
        border-radius: 25px;
        padding: 5px;
        padding-top: 20px;
        """
        info_danger = """
        background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(203, 206, 65, 1), stop:1 rgba(203, 206, 65, 0));
        border: none;
        border-radius: 25px;
        padding: 5px;
        padding-top: 20px;
        """
        return {'success': info_success, 'danger': info_danger, 'error': info_error}

    def show_category_edit(self):
        self.ui.frame_name_category_edit.setVisible(True)
        self.ui.frame_element_edit.setVisible(False)

    def show_element_edit(self):
        self.ui.frame_name_category_edit.setVisible(False)
        self.ui.frame_element_edit.setVisible(True)

    # def show_element_edit_anim(self):
    #     frame_height = self.ui.frame_element_edit.height()
    #     print(frame_height)
    #     width = 0
    #     if frame_height == 0:
    #         width = 250
    #     # Start animation
    #     self.animation = QPropertyAnimation(self.ui.frame_element_edit, b"maximumHeight")
    #     self.animation.setStartValue(frame_height)
    #     self.animation.setEndValue(width)
    #     self.animation.setDuration(700)
    #     self.animation.setEasingCurve(QEasingCurve.InOutCubic)
    #     self.animation.start()
    #
    # def category_animation(self):
    #     frame_height = self.ui.frame_name_category_edit.height()
    #     width = 0
    #     if frame_height == 0:
    #         width = 74
    #     # Start animation
    #     self.animation = QPropertyAnimation(self.ui.frame_name_category_edit, b"maximumHeight")
    #     self.animation.setStartValue(frame_height)
    #     self.animation.setEndValue(width)
    #     self.animation.setDuration(700)
    #     self.animation.setEasingCurve(QEasingCurve.InOutCubic)
    #     self.animation.start()


    def animation_info(self, info_panel):
        info_panel_height = info_panel.height()
        width = 0
        if info_panel_height == 0:
            width = 400
          # Start animation
        self.animation = QPropertyAnimation(info_panel,  b"maximumHeight")
        self.animation.setStartValue(info_panel_height)
        self.animation.setKeyValueAt(0.25, width)
        self.animation.setEndValue(info_panel_height)
        self.animation.setDuration(700)
        self.animation.setEasingCurve(QEasingCurve.InBack)
        self.animation.start()

# Определение ОС
    def check_os_type(self):
        if os.name == 'posix':
            desc = QApplication.desktop()
            self.move(desc.availableGeometry().center() - self.rect().center())
        else:
            pass

# вызывается при нажатии кнопки мыши по форме
    def mousePressEvent(self, event):
        # Если нажата левая кнопка мыши
        if event.button() == QtCore.Qt.LeftButton:
            # получаем координаты окна относительно экрана
            x_main = self.geometry().x()
            y_main = self.geometry().y()
            # получаем координаты курсора относительно окна нашей программы
            cursor_x = QtGui.QCursor.pos().x()
            cursor_y = QtGui.QCursor.pos().y()
            # проверяем условием позицию курсора на нужной области программы(у нас это верхний бар)
            # если всё ок - перемещаем
            # иначе игнорируем
            if x_main <= cursor_x <= x_main + self.geometry().width():
                if y_main <= cursor_y <= y_main + self.ui.frame_header.geometry().height():
                    self.old_pos = event.pos()
                else:
                    self.old_pos = None
        elif event.button() == QtCore.Qt.RightButton:
            self.old_pos = None

    # вызывается при отпускании кнопки мыши
    def mouseReleaseEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.old_pos = None

    # вызывается всякий раз, когда мышь перемещается
    def mouseMoveEvent(self, event):
        if not self.old_pos:
            return
        delta = event.pos() - self.old_pos
        self.move(self.pos() + delta)

    def on_min(self):
        self.showMinimized()

    #Диалог закрытия приложения
    def closeEvent(self):
        # Переопределить colseEvent
        reply = QMessageBox.question \
            (self, 'Выход из приложения',
             "Вы уверены, что хотите уйти?",
             QMessageBox.Yes,
             QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit()
        else:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Doug's Application")
    window = MainWindow(app)
    app.exec_()