from qt_core import *
import os

class SettingsUi():
    def __init__(self, parent):
        app_path = os.path.abspath(os.getcwd())
        folder_img = "gui/images"
        path = os.path.join(app_path, folder_img)
        icon_path_label = os.path.normpath(os.path.join(path, "label.png"))
        icon_path_icon = os.path.normpath(os.path.join(path, "icon.png"))
        icon_path_edit_reestr = os.path.normpath(os.path.join(path, "edit_reestr.png"))
        icon_path_setting = os.path.normpath(os.path.join(path, "XMLID_273_.png"))
        icon_path_table = os.path.normpath(os.path.join(path, "table.png"))
        icon_path_roll_up_btn = os.path.normpath(os.path.join(path, "line.png"))
        icon_path_exit = os.path.normpath(os.path.join(path, "exit.png"))
        icon_path_git = os.path.normpath(os.path.join(path, "icons8-github-48.png"))
        icon_path_key = os.path.normpath(os.path.join(path, "key.png"))
        icon_path_db = os.path.normpath(os.path.join(path, "database.png"))
        icon_path_menu = os.path.normpath(os.path.join(path, "menu.png"))

        icon = QIcon()
        icon.addFile(icon_path_menu, QSize(), QIcon.Normal, QIcon.Off)
        parent.main_menu_page_edit_btn.setIcon(icon)
        parent.main_menu_page_edit_btn.setIconSize(QSize(20, 20))

        icon = QIcon()
        icon.addFile(icon_path_menu, QSize(), QIcon.Normal, QIcon.Off)
        parent.main_menu_btn_set.setIcon(icon)
        parent.main_menu_btn_set.setIconSize(QSize(20, 20))

        icon = QIcon()
        icon.addFile(icon_path_menu, QSize(), QIcon.Normal, QIcon.Off)
        parent.go_back_menu_reestr.setIcon(icon)
        parent.go_back_menu_reestr.setIconSize(QSize(20, 20))

        icon = QIcon()
        icon.addFile(icon_path_key, QSize(), QIcon.Normal, QIcon.Off)
        parent.key_btn.setIcon(icon)
        parent.key_btn.setIconSize(QSize(20, 20))

        icon = QIcon()
        icon.addFile(icon_path_db, QSize(), QIcon.Normal, QIcon.Off)
        parent.db_btn.setIcon(icon)
        parent.db_btn.setIconSize(QSize(20, 20))

        icon = QIcon()
        icon.addFile(icon_path_git, QSize(), QIcon.Normal, QIcon.Off)
        parent.git_btn.setIcon(icon)
        parent.git_btn.setIconSize(QSize(20, 20))

        icon = QIcon()
        icon.addFile(icon_path_git, QSize(), QIcon.Normal, QIcon.Off)
        parent.git_btn.setIcon(icon)
        parent.git_btn.setIconSize(QSize(20, 20))

        parent.label_7.setPixmap(QPixmap(icon_path_icon))
        parent.label_5.setPixmap(QPixmap(icon_path_label))
        icon = QIcon()
        icon.addFile(icon_path_setting, QSize(), QIcon.Normal, QIcon.Off)
        parent.btn_settings.setIcon(icon)
        parent.btn_settings.setIconSize(QSize(140, 170))
        icon = QIcon()
        icon.addFile(icon_path_edit_reestr, QSize(), QIcon.Normal, QIcon.Off)
        parent.btn_edit_pass_reestr.setIcon(icon)
        parent.btn_edit_pass_reestr.setIconSize(QSize(182, 178))
        icon = QIcon()
        icon.addFile(icon_path_table, QSize(), QIcon.Normal, QIcon.Off)
        parent.btn_pass_reestr.setIcon(icon)
        parent.btn_pass_reestr.setIconSize(QSize(182, 178))
        icon = QIcon()
        icon.addFile(icon_path_roll_up_btn, QSize(), QIcon.Normal, QIcon.Off)
        parent.roll_up_btn.setIcon(icon)
        icon = QIcon()
        icon.addFile(icon_path_exit, QSize(), QIcon.Normal, QIcon.Off)
        parent.exit_btn.setIcon(icon)



