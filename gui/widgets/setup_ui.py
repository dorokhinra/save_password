from qt_core import *
import os

class SettingsUi():
    def __init__(self, parent):
        app_path = os.path.abspath(os.getcwd())
        folder_img = "gui/images"
        path = os.path.join(app_path, folder_img)
        icon_path_label = os.path.normpath(os.path.join(path, "label.png"))
        icon_path_icon = os.path.normpath(os.path.join(path, "icon.png"))
        parent.label_7.setPixmap(QPixmap(icon_path_icon))
        parent.label_5.setPixmap(QPixmap(icon_path_label))