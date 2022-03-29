
from qt_core import *
from PyQt5 import QtCore, QtWidgets


class ContextMenuOn(QtWidgets.QMenu):

    def __init__(self, del_widget):
        super().__init__()
        self.row_index = ''
        self.id = ''
        self.del_widget = del_widget

    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_custom_context_menu(self, pos):
        if self.sender().currentIndex().row() == -1:
            return
        widget = self.sender()
        if isinstance(widget, QtWidgets.QAbstractItemView):
            widget = widget.viewport()
        menu = QtWidgets.QMenu()
        delete_item = QAction("Удалить элемент из списка", menu)
        # Добавляем заголовки в меню
        menu.addAction(delete_item)
        # STYLE
        style = self.menu_style()
        menu.setStyleSheet(style)
        index = self.sender().currentIndex()
        # Отлов Наша таблица
        wid = self.sender()
        # menu_del.triggered.connect(self.DelWidget)
        self.id = index.data(Qt.UserRole)
        delete_item.triggered.connect(lambda: self.del_widget(self.id))
        menu.exec_(widget.mapToGlobal(pos))

    def menu_style(self):
        style = """
                QMenu {
                background-color: #21232d;
                font-size: 10pt;
                padding: 10px;
                border: 1px solid rgba(198,0,124, 0.7);
                border-radius: 6px;
                }
                QMenu::item {

               color: rgb(255, 255, 255);
               }
                QMenu::item:selected {
               background-color: rgba(198,0,124, 0.2);
               color: rgb(255, 255, 255);
               }
            """
        return style

class ContextMenuForTableElem(QtWidgets.QMenu):
    def __init__(self, decrypt_elem):
        super().__init__()
        self.row_index = ''
        self.row = ''
        self.decrypt_elem = decrypt_elem

    @QtCore.pyqtSlot(QtCore.QPoint)
    def on_custom_context_menu(self, pos):
        if self.sender().currentIndex().row() == -1:
            return
        widget = self.sender()
        if isinstance(widget, QtWidgets.QAbstractItemView):
            widget = widget.viewport()
        menu = QtWidgets.QMenu()
        decrypt_item = QAction("Расшифровать", menu)
        # Добавляем заголовки в меню
        menu.addAction(decrypt_item)
        # STYLE
        style = self.menu_style()
        menu.setStyleSheet(style)
        index = self.sender().currentIndex()
        # Отлов Наша таблица
        wid = self.sender()
        # menu_del.triggered.connect(self.DelWidget)
        self.row = index.row()
        decrypt_item.triggered.connect(lambda: self.decrypt_elem(wid, index))
        menu.exec_(widget.mapToGlobal(pos))

    def menu_style(self):
        style = """
                QMenu {
                background-color: #21232d;
                font-size: 10pt;
                padding: 10px;
                border: 1px solid rgba(198,0,124, 0.7);
                border-radius: 6px;
                }
                QMenu::item {

               color: rgb(255, 255, 255);
               }
                QMenu::item:selected {
               background-color: rgba(198,0,124, 0.2);
               color: rgb(255, 255, 255);
               }
            """
        return style




