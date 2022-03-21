#IMPORT MUDULES
import os
import glob
import sys
import time
#IMPORT QTQORE
from qt_core import *
# UI
from gui.windows.ui_main_ui import Ui_MainWindow

#SETTING_UI
from gui.widgets.setup_ui import SettingsUi

#БаЗа Данных
from database.session import DbSession

#MAIN_WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

#########
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        SettingsUi(self.ui)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.ui.roll_up_btn.clicked.connect(self.on_min)
        self.ui.exit_btn.clicked.connect(self.closeEvent)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        self.ui.btn_settings.clicked.connect(self.show_settings)
        self.ui.btn_pass_reestr.clicked.connect(self.show_reestr)
        self.ui.btn_edit_pass_reestr.clicked.connect(self.show_edit_reestr)

        #установка первой страницей синхронизации с базой данных
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4)

        #Кнопки переключения для страници с настройками
        self.ui.main_menu_btn_set.clicked.connect(self.go_to_back)
        self.ui.git_btn.clicked.connect(self.show_git_settings)
        self.ui.key_btn.clicked.connect(self.show_key_settings)
        self.ui.db_btn.clicked.connect(self.show_db_settings)

        #Кнопки на странице изменения реестра
        self.ui.main_menu_page_edit_btn.clicked.connect(self.go_to_back)

        #Кнопка переключения главного меню для реестра
        self.ui.go_back_menu_reestr.clicked.connect(self.go_to_back)

        #БАЗА дАННЫХ
        self.check_db()

        self.ui.pushButton.clicked.connect(self.create_db)


        self.check_os_type()
        self.show()

    def check_db(self):
        app_path = os.path.abspath(os.getcwd())
        folder = "database/db_file"
        path = os.path.join(app_path, folder)
        path_db = os.path.normpath(os.path.join(path, "password_store.sqlite"))
        if os.path.exists(path_db):
            self.db = DbSession()
            self.db.create_table(self.db.session)
        else:
            self.ui.label_info_db.setText("Базы данных не существует!")

    def create_db(self):
        if self.ui.db_login_edit.text() is not '' and self.ui.db_pass_edit.text() is not '':
            if self.ui.radioButton.isChecked():
                self.db = DbSession()
                self.db.create_table(self.db.session)
                self.ui.label_info_db.setText("")
                self.ui.pushButton.setEnabled(False)
        else:
            self.ui.label_info_db.setText("Заполнены не все поля!")

    def show_db_settings(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_6)

    def show_git_settings(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_4)

    def show_key_settings(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_5)

    def show_settings(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def show_reestr(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)

    def go_to_back(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)

    def show_edit_reestr(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_edit)

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
    window = MainWindow()
    app.exec_()