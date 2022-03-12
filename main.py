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
        self.show()

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