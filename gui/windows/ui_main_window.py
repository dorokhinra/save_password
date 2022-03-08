#IMPORT QT_CORE
from qt_core import *


class UI_MainWindow(object):

    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        #УСТАНОВИТЬ МИНИМАЛЬНЫЕ ЗНАЧЕНИЯ
        parent.resize(1100, 700)
        parent.setMinimumSize(1060, 640)