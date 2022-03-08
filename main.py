#IMPORT MUDULES
import os
import glob
import sys
import time
#IMPORT QTQORE
from qt_core import *
# UI
from gui.windows.ui_main_window import UI_MainWindow

#MAIN_WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

#########

        # Окно по центру
        desc = QApplication.desktop()
        self.move(desc.availableGeometry().center() - self.rect().center())
        self.ui = UI_MainWindow(self)
        self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()