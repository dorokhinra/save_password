# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uirFrCPt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

import gui.resources.res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 738)
        MainWindow.setMinimumSize(QSize(1000, 738))
        MainWindow.setMaximumSize(QSize(1000, 738))
        MainWindow.setStyleSheet(u"QWidget{\n"
"border:none;\n"
"}\n"
"QMainWindow {\n"
"border: 3px   solid rgba(37, 48, 38, 1);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 738))
        self.centralwidget.setMaximumSize(QSize(1000, 738))
        self.centralwidget.setStyleSheet(u"background-color: rgba(36, 36, 36, 1);")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_header = QFrame(self.centralwidget)
        self.frame_header.setObjectName(u"frame_header")
        self.frame_header.setMinimumSize(QSize(0, 40))
        self.frame_header.setMaximumSize(QSize(16777215, 40))
        self.frame_header.setStyleSheet(u"background-color: rgba(37, 48, 38, 1);\n"
"color: rgba(255, 255, 255, 1);")
        self.frame_header.setFrameShape(QFrame.StyledPanel)
        self.frame_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_header)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_header)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setPixmap(QPixmap(u"../../prototype/icon.png"))

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_6 = QLabel(self.frame_header)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.roll_up_btn = QPushButton(self.frame_header)
        self.roll_up_btn.setObjectName(u"roll_up_btn")
        self.roll_up_btn.setMinimumSize(QSize(40, 0))
        self.roll_up_btn.setMaximumSize(QSize(40, 40))
        self.roll_up_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(216, 216, 216, 0.0);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(197, 197, 197, 0.4);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(216, 216, 216, 0.2);\n"
"}")
        icon = QIcon()
        icon.addFile(u"../images/line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.roll_up_btn.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.roll_up_btn)

        self.exit_btn = QPushButton(self.frame_header)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setMinimumSize(QSize(40, 0))
        self.exit_btn.setMaximumSize(QSize(40, 40))
        self.exit_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(216, 216, 216, 0.0);\n"
"	border: none;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(182, 56, 7);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(182, 56, 7, 0.4);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../images/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_btn.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.exit_btn)


        self.verticalLayout_3.addWidget(self.frame_header)

        self.frame_body = QFrame(self.centralwidget)
        self.frame_body.setObjectName(u"frame_body")
        self.frame_body.setStyleSheet(u"background-color: rgba(36, 36, 36, 1);\n"
"color: rgba(255, 255, 255, 1);")
        self.frame_body.setFrameShape(QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_body)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_2 = QVBoxLayout(self.page_1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 227))
        self.frame.setMaximumSize(QSize(16777215, 227))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(117, 231, 163, 1), stop:1 rgba(117, 231, 163, 0));\n"
"border:none;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(230, 178))
        self.label_5.setMaximumSize(QSize(230, 178))
        self.label_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.0);")
        self.label_5.setPixmap(QPixmap(u"../../prototype/label.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_5)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 40))
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.0);\n"
"font: 20pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_3.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";\n"
"border:none;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_setting_btn = QFrame(self.frame_2)
        self.frame_setting_btn.setObjectName(u"frame_setting_btn")
        self.frame_setting_btn.setMinimumSize(QSize(178, 0))
        self.frame_setting_btn.setMaximumSize(QSize(178, 16777215))
        self.frame_setting_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_setting_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_setting_btn)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.btn_settings = QPushButton(self.frame_setting_btn)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(178, 182))
        self.btn_settings.setMaximumSize(QSize(178, 182))
        self.btn_settings.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgba(195, 195, 195, 0.7);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(197, 197, 197, 0.4);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(216, 216, 216, 0.2);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../images/XMLID_273_.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon2)
        self.btn_settings.setIconSize(QSize(140, 170))

        self.verticalLayout_4.addWidget(self.btn_settings)

        self.label = QLabel(self.frame_setting_btn)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.frame_setting_btn)

        self.frame_reestr_btn = QFrame(self.frame_2)
        self.frame_reestr_btn.setObjectName(u"frame_reestr_btn")
        self.frame_reestr_btn.setMinimumSize(QSize(185, 0))
        self.frame_reestr_btn.setMaximumSize(QSize(178, 16777215))
        self.frame_reestr_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_reestr_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_reestr_btn)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.btn_pass_reestr = QPushButton(self.frame_reestr_btn)
        self.btn_pass_reestr.setObjectName(u"btn_pass_reestr")
        self.btn_pass_reestr.setMinimumSize(QSize(178, 182))
        self.btn_pass_reestr.setMaximumSize(QSize(178, 182))
        self.btn_pass_reestr.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgba(195, 195, 195, 0.7);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(197, 197, 197, 0.4);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(216, 216, 216, 0.2);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../../prototype/table.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_pass_reestr.setIcon(icon3)
        self.btn_pass_reestr.setIconSize(QSize(178, 182))
        self.btn_pass_reestr.setCheckable(False)

        self.verticalLayout_5.addWidget(self.btn_pass_reestr)

        self.label_2 = QLabel(self.frame_reestr_btn)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)


        self.horizontalLayout_2.addWidget(self.frame_reestr_btn)

        self.frame_edit_btn = QFrame(self.frame_2)
        self.frame_edit_btn.setObjectName(u"frame_edit_btn")
        self.frame_edit_btn.setMinimumSize(QSize(185, 0))
        self.frame_edit_btn.setMaximumSize(QSize(188, 16777215))
        self.frame_edit_btn.setFrameShape(QFrame.StyledPanel)
        self.frame_edit_btn.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_edit_btn)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.btn_edit_pass_reestr = QPushButton(self.frame_edit_btn)
        self.btn_edit_pass_reestr.setObjectName(u"btn_edit_pass_reestr")
        self.btn_edit_pass_reestr.setMinimumSize(QSize(178, 182))
        self.btn_edit_pass_reestr.setMaximumSize(QSize(178, 182))
        self.btn_edit_pass_reestr.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgba(195, 195, 195, 0.7);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(197, 197, 197, 0.4);\n"
"border:none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(216, 216, 216, 0.2);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../images/edit_reestr.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit_pass_reestr.setIcon(icon4)
        self.btn_edit_pass_reestr.setIconSize(QSize(178, 182))

        self.verticalLayout_6.addWidget(self.btn_edit_pass_reestr)

        self.label_3 = QLabel(self.frame_edit_btn)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)


        self.horizontalLayout_2.addWidget(self.frame_edit_btn)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.horizontalLayout_5 = QHBoxLayout(self.page_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.set_panel = QFrame(self.page_2)
        self.set_panel.setObjectName(u"set_panel")
        self.set_panel.setMinimumSize(QSize(250, 0))
        self.set_panel.setMaximumSize(QSize(250, 16777215))
        self.set_panel.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"Sans Serif\";\n"
"	background-color: rgba(195, 195, 195, 0.7);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(197, 197, 197, 0.4);\n"
"border: 3px   solid rgba(37, 48, 38, 1);\n"
"	 \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(216, 216, 216, 0.2);\n"
"}")
        self.set_panel.setFrameShape(QFrame.StyledPanel)
        self.set_panel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.set_panel)
        self.verticalLayout_7.setSpacing(9)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(15, -1, 15, -1)
        self.git_btn = QPushButton(self.set_panel)
        self.git_btn.setObjectName(u"git_btn")
        self.git_btn.setMinimumSize(QSize(0, 50))
        icon5 = QIcon()
        icon5.addFile(u"../images/icons8-github-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.git_btn.setIcon(icon5)
        self.git_btn.setIconSize(QSize(25, 25))

        self.verticalLayout_7.addWidget(self.git_btn)

        self.key_btn = QPushButton(self.set_panel)
        self.key_btn.setObjectName(u"key_btn")
        self.key_btn.setMinimumSize(QSize(0, 50))
        self.key_btn.setLayoutDirection(Qt.LeftToRight)
        icon6 = QIcon()
        icon6.addFile(u"../images/key.png", QSize(), QIcon.Normal, QIcon.Off)
        self.key_btn.setIcon(icon6)
        self.key_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_7.addWidget(self.key_btn)

        self.db_btn = QPushButton(self.set_panel)
        self.db_btn.setObjectName(u"db_btn")
        self.db_btn.setMinimumSize(QSize(0, 50))
        icon7 = QIcon()
        icon7.addFile(u"../images/database.png", QSize(), QIcon.Normal, QIcon.Off)
        self.db_btn.setIcon(icon7)
        self.db_btn.setIconSize(QSize(20, 20))

        self.verticalLayout_7.addWidget(self.db_btn)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)

        self.main_menu_btn_set = QPushButton(self.set_panel)
        self.main_menu_btn_set.setObjectName(u"main_menu_btn_set")
        self.main_menu_btn_set.setMinimumSize(QSize(0, 50))
        icon8 = QIcon()
        icon8.addFile(u"../images/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.main_menu_btn_set.setIcon(icon8)

        self.verticalLayout_7.addWidget(self.main_menu_btn_set)


        self.horizontalLayout_5.addWidget(self.set_panel)

        self.frame_4 = QFrame(self.page_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stackedWidget_2 = QStackedWidget(self.frame_4)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_9 = QVBoxLayout(self.page_4)
        self.verticalLayout_9.setSpacing(1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_16 = QFrame(self.page_4)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 50))
        self.frame_16.setStyleSheet(u"#frame_16 {\n"
"	background-image: url(:/images/fon.png);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"#frame_18 {\n"
"background-color: rgba(36, 36, 36, 0.9);\n"
"border-radius: 20px;\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_16)
        self.verticalLayout_20.setSpacing(1)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 40))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_18)
        self.verticalLayout_22.setSpacing(1)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_18)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 40))
        self.label_10.setMaximumSize(QSize(16777215, 40))
        self.label_10.setStyleSheet(u"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"font: 14pt \"Sans Serif\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(117, 231, 163, 1), stop:1 rgba(117, 231, 163, 0));")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_10)

        self.frame_7 = QFrame(self.frame_18)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"\n"
"#frame_7{\n"
"font: 14pt \"Sans Serif\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(117, 231, 163, 1), stop:1 rgba(117, 231, 163, 0));\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setSpacing(1)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(20, -1, 20, -1)
        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_14.addItem(self.verticalSpacer_11)

        self.token_edit = QLineEdit(self.frame_7)
        self.token_edit.setObjectName(u"token_edit")
        self.token_edit.setMinimumSize(QSize(0, 40))
        self.token_edit.setStyleSheet(u"QLineEdit {\n"
"border-radius: 10px;\n"
"background-color: rgba(36, 36, 36, 0.9);\n"
"border: 3px   solid rgba(37, 48, 38, 1);	 \n"
"padding: 5px;\n"
"}")
        self.token_edit.setEchoMode(QLineEdit.Password)

        self.verticalLayout_14.addWidget(self.token_edit)

        self.label_info_sinc = QLabel(self.frame_7)
        self.label_info_sinc.setObjectName(u"label_info_sinc")
        self.label_info_sinc.setStyleSheet(u"color: rgb(234, 78, 117);\n"
"background-color: rgba(255, 255, 255, 0.0);")

        self.verticalLayout_14.addWidget(self.label_info_sinc)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QFrame {\n"
"	background-color: rgba(255, 255, 255, 0.0);\n"
"border: none;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_8)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setContentsMargins(-1, 15, -1, -1)
        self.btn_sinc = QPushButton(self.frame_8)
        self.btn_sinc.setObjectName(u"btn_sinc")
        self.btn_sinc.setMinimumSize(QSize(100, 40))
        self.btn_sinc.setMaximumSize(QSize(200, 16777215))
        self.btn_sinc.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"Sans Serif\";\n"
"	background-color: rgba(37, 48, 38, 0.7);\n"
"\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(37, 48, 38, 1);\n"
"border: 3px   solid rgba(195, 195, 195, 0.7);;\n"
"	 \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(216, 216, 216, 0.2);\n"
"}")

        self.gridLayout_2.addWidget(self.btn_sinc, 0, 0, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_10, 1, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.frame_8)


        self.verticalLayout_22.addWidget(self.frame_7)


        self.verticalLayout_20.addWidget(self.frame_18)


        self.verticalLayout_9.addWidget(self.frame_16)

        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_10 = QVBoxLayout(self.page_5)
        self.verticalLayout_10.setSpacing(1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_20 = QFrame(self.page_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 40))
        self.frame_20.setStyleSheet(u"#frame_20 { \n"
"background-image: url(:/images/fon.png);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"#frame_19 {\n"
"background-color: rgba(36, 36, 36, 0.9);\n"
"border-radius: 20px;\n"
"}")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_20)
        self.verticalLayout_24.setSpacing(1)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.frame_19 = QFrame(self.frame_20)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 40))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_19)
        self.verticalLayout_23.setSpacing(1)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_19)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 40))
        self.label_11.setMaximumSize(QSize(16777215, 40))
        self.label_11.setStyleSheet(u"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"font: 14pt \"Sans Serif\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(117, 231, 163, 1), stop:1 rgba(117, 231, 163, 0));")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_11)

        self.frame_9 = QFrame(self.frame_19)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"#frame_9{\n"
"font: 14pt \"Sans Serif\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(117, 231, 163, 1), stop:1 rgba(117, 231, 163, 0));\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_9)
        self.verticalLayout_15.setSpacing(1)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(20, -1, 20, -1)
        self.verticalSpacer_13 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_15.addItem(self.verticalSpacer_13)

        self.textEdit = QTextEdit(self.frame_9)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 110))
        self.textEdit.setMaximumSize(QSize(16777215, 110))
        self.textEdit.setStyleSheet(u"background-color: rgba(206, 152, 17, 0.6);\n"
"border: none;\n"
"border-radius: 25px;\n"
"padding: 5px;\n"
"")

        self.verticalLayout_15.addWidget(self.textEdit)

        self.verticalSpacer_14 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_15.addItem(self.verticalSpacer_14)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 50))
        self.frame_11.setStyleSheet(u"border: none;\n"
"background-color: rgba(255, 255, 255, 0.0);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_11)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.edit_pass_key = QLineEdit(self.frame_11)
        self.edit_pass_key.setObjectName(u"edit_pass_key")
        self.edit_pass_key.setMinimumSize(QSize(0, 40))
        self.edit_pass_key.setStyleSheet(u"QLineEdit {\n"
"border-radius: 10px;\n"
"background-color: rgba(36, 36, 36, 0.9);\n"
"border: 3px   solid rgba(37, 48, 38, 1);	 \n"
"padding: 5px;\n"
"}")
        self.edit_pass_key.setEchoMode(QLineEdit.Password)

        self.verticalLayout_16.addWidget(self.edit_pass_key)

        self.info_key = QLabel(self.frame_11)
        self.info_key.setObjectName(u"info_key")
        self.info_key.setContextMenuPolicy(Qt.NoContextMenu)
        self.info_key.setStyleSheet(u"color: rgb(234, 78, 117);")

        self.verticalLayout_16.addWidget(self.info_key)


        self.verticalLayout_15.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.0);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_10)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_12, 2, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_6, 0, 2, 1, 1)

        self.btn_add_key = QPushButton(self.frame_10)
        self.btn_add_key.setObjectName(u"btn_add_key")
        self.btn_add_key.setMinimumSize(QSize(200, 40))
        self.btn_add_key.setMaximumSize(QSize(16777215, 40))
        self.btn_add_key.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"Sans Serif\";\n"
"	background-color: rgba(37, 48, 38, 0.7);\n"
"\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(37, 48, 38, 1);\n"
"border: 3px   solid rgba(195, 195, 195, 0.7);;\n"
"	 \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(216, 216, 216, 0.2);\n"
"}")

        self.gridLayout_3.addWidget(self.btn_add_key, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_10)


        self.verticalLayout_23.addWidget(self.frame_9)


        self.verticalLayout_24.addWidget(self.frame_19)


        self.verticalLayout_10.addWidget(self.frame_20)

        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_11 = QVBoxLayout(self.page_6)
        self.verticalLayout_11.setSpacing(1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_15 = QFrame(self.page_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 40))
        self.frame_15.setStyleSheet(u"#frame_15 { \n"
"background-image: url(:/images/fon.png);\n"
"border-radius: 20px;\n"
"}\n"
"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_15)
        self.verticalLayout_19.setSpacing(1)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 40))
        self.frame_17.setStyleSheet(u"#frame_17 {\n"
"background-color: rgba(36, 36, 36, 0.9);\n"
"border-radius: 20px;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_17)
        self.verticalLayout_21.setSpacing(1)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_17)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 40))
        self.label_8.setMaximumSize(QSize(16777215, 40))
        self.label_8.setStyleSheet(u"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"font: 14pt \"Sans Serif\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(117, 231, 163, 1), stop:1 rgba(117, 231, 163, 0));")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_8)

        self.frame_6 = QFrame(self.frame_17)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"border:none;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(117, 231, 163, 1), stop:1 rgba(117, 231, 163, 0.2));\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setContentsMargins(20, -1, 20, 10)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 7, 0, 1, 1)

        self.db_pass_edit = QLineEdit(self.frame_6)
        self.db_pass_edit.setObjectName(u"db_pass_edit")
        self.db_pass_edit.setMinimumSize(QSize(0, 40))
        self.db_pass_edit.setStyleSheet(u"QLineEdit {\n"
"border-radius: 10px;\n"
"background-color: rgba(36, 36, 36, 0.9);\n"
"border: 3px   solid rgba(37, 48, 38, 1);	 \n"
"padding: 5px;\n"
"}")
        self.db_pass_edit.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.db_pass_edit, 5, 0, 1, 3)

        self.verticalSpacer_15 = QSpacerItem(0, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_15, 4, 0, 1, 3)

        self.radioButton_2 = QRadioButton(self.frame_6)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"QRadioButton {\n"
"background-color: rgba(85, 255, 0, 0.0);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"border: 3px solid; \n"
"border-color: rgba(37, 48, 38, 0.7);\n"
"width: 40px;\n"
"height: 25px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{ \n"
"border: 3px solid; \n"
"border-color: rgba(37, 48, 38, 0.7);\n"
"border-radius: 5px;\n"
"background-color: rgba(195, 195, 195, 0.7);\n"
"width: 40px;\n"
"height: 25px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{ \n"
"border: 3px solid; \n"
"border-color: rgba(37, 48, 38, 0.9);\n"
"border-radius: 6px;\n"
"background-color: rgba(255, 131, 23, 0.7);\n"
"width: 40px;\n"
"height: 25px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.radioButton_2, 1, 1, 1, 1)

        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(200, 40))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"Sans Serif\";\n"
"	background-color: rgba(37, 48, 38, 0.7);\n"
"\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(37, 48, 38, 1);\n"
"border: 3px   solid rgba(195, 195, 195, 0.7);;\n"
"	 \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(216, 216, 216, 0.2);\n"
"}")

        self.gridLayout.addWidget(self.pushButton, 7, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_9, 0, 0, 1, 3)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_8, 8, 1, 1, 1)

        self.db_login_edit = QLineEdit(self.frame_6)
        self.db_login_edit.setObjectName(u"db_login_edit")
        self.db_login_edit.setMinimumSize(QSize(0, 40))
        self.db_login_edit.setStyleSheet(u"QLineEdit {\n"
"border-radius: 10px;\n"
"background-color: rgba(36, 36, 36, 0.9);\n"
"border: 3px   solid rgba(37, 48, 38, 1);	 \n"
"padding: 5px;\n"
"}")

        self.gridLayout.addWidget(self.db_login_edit, 3, 0, 1, 3)

        self.radioButton = QRadioButton(self.frame_6)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"QRadioButton {\n"
"	background-color: rgba(85, 255, 0, 0.0);\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"border: 3px solid; \n"
"border-color: rgba(37, 48, 38, 0.7);\n"
"width: 40px;\n"
"height: 25px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked{ \n"
"border: 3px solid; \n"
"border-color: rgba(37, 48, 38, 0.7);\n"
"border-radius: 5px;\n"
"background-color: rgba(195, 195, 195, 0.7);\n"
"width: 40px;\n"
"height: 25px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked{ \n"
"border: 3px solid; \n"
"border-color: rgba(37, 48, 38, 0.9);\n"
"border-radius: 6px;\n"
"background-color: rgba(255, 131, 23, 0.7);\n"
"width: 40px;\n"
"height: 25px;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.radioButton, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 7, 2, 1, 1)

        self.label_info_db = QLabel(self.frame_6)
        self.label_info_db.setObjectName(u"label_info_db")
        self.label_info_db.setMaximumSize(QSize(16777215, 25))
        self.label_info_db.setStyleSheet(u"color: rgb(234, 78, 117);\n"
"background-color: rgba(255, 255, 255, 0.0);")

        self.gridLayout.addWidget(self.label_info_db, 6, 0, 1, 1)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_16, 2, 0, 1, 3)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_17, 6, 1, 1, 1)


        self.verticalLayout_21.addWidget(self.frame_6)


        self.verticalLayout_19.addWidget(self.frame_17)


        self.verticalLayout_11.addWidget(self.frame_15)

        self.stackedWidget_2.addWidget(self.page_6)

        self.verticalLayout_8.addWidget(self.stackedWidget_2)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_7 = QHBoxLayout(self.page_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_5 = QFrame(self.page_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(250, 0))
        self.frame_5.setMaximumSize(QSize(250, 16777215))
        self.frame_5.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"Sans Serif\";\n"
"	background-color: rgba(195, 195, 195, 0.7);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(197, 197, 197, 0.4);\n"
"border: 3px   solid rgba(37, 48, 38, 1);\n"
"	 \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(216, 216, 216, 0.2);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 40))
        self.label_9.setMaximumSize(QSize(16777215, 30))
        self.label_9.setStyleSheet(u"font: 12pt \"Sans Serif\";\n"
"border-bottom: 2px   solid rgb(184, 184, 184);\n"
"background-color: rgba(37, 48, 38, 1);\n"
"border-radius: 5px;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_9)

        self.reestr_tree_frame = QFrame(self.frame_5)
        self.reestr_tree_frame.setObjectName(u"reestr_tree_frame")
        self.reestr_tree_frame.setFrameShape(QFrame.StyledPanel)
        self.reestr_tree_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.reestr_tree_frame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.treeView = QTreeView(self.reestr_tree_frame)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout_12.addWidget(self.treeView)


        self.verticalLayout.addWidget(self.reestr_tree_frame)

        self.go_back_menu_reestr = QPushButton(self.frame_5)
        self.go_back_menu_reestr.setObjectName(u"go_back_menu_reestr")
        self.go_back_menu_reestr.setMinimumSize(QSize(0, 50))
        self.go_back_menu_reestr.setIcon(icon8)
        self.go_back_menu_reestr.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.go_back_menu_reestr)


        self.horizontalLayout_7.addWidget(self.frame_5)

        self.frame_3 = QFrame(self.page_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"#frame_3{\n"
"	background-color: rgba(195, 195, 195, 0.3);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.tableView = QTableView(self.frame_3)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_13.addWidget(self.tableView)


        self.horizontalLayout_7.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_3)
        self.page_edit = QWidget()
        self.page_edit.setObjectName(u"page_edit")
        self.horizontalLayout_8 = QHBoxLayout(self.page_edit)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_12 = QFrame(self.page_edit)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(250, 0))
        self.frame_12.setMaximumSize(QSize(250, 16777215))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_12)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_17 = QLabel(self.frame_12)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 40))
        self.label_17.setStyleSheet(u"font: 12pt \"Sans Serif\";\n"
"border-bottom: 2px   solid rgb(184, 184, 184);\n"
"background-color: rgba(37, 48, 38, 1);\n"
"border-radius: 5px;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_17)

        self.treeView_2 = QTreeView(self.frame_12)
        self.treeView_2.setObjectName(u"treeView_2")

        self.verticalLayout_18.addWidget(self.treeView_2)

        self.main_menu_page_edit_btn = QPushButton(self.frame_12)
        self.main_menu_page_edit_btn.setObjectName(u"main_menu_page_edit_btn")
        self.main_menu_page_edit_btn.setMinimumSize(QSize(0, 50))
        self.main_menu_page_edit_btn.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"Sans Serif\";\n"
"	background-color: rgba(195, 195, 195, 0.7);\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(197, 197, 197, 0.4);\n"
"border: 3px   solid rgba(37, 48, 38, 1);\n"
"	 \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(216, 216, 216, 0.2);\n"
"}")
        self.main_menu_page_edit_btn.setIcon(icon8)

        self.verticalLayout_18.addWidget(self.main_menu_page_edit_btn)

        self.main_menu_page_edit_btn.raise_()
        self.treeView_2.raise_()
        self.label_17.raise_()

        self.horizontalLayout_8.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.page_edit)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"#frame_13{\n"
"	background-color: rgba(195, 195, 195, 0.3);\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setSpacing(1)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 40))
        self.label_18.setMaximumSize(QSize(16777215, 40))
        self.label_18.setStyleSheet(u"font: 12pt \"Sans Serif\";\n"
"background-color: rgba(37, 48, 38, 1);\n"
"")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_18)

        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.frame_14)


        self.horizontalLayout_8.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.page_edit)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.frame_body)

        self.frame_footer = QFrame(self.centralwidget)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setMinimumSize(QSize(0, 40))
        self.frame_footer.setMaximumSize(QSize(16777215, 40))
        self.frame_footer.setStyleSheet(u"background-color: rgba(37, 48, 38, 1);\n"
"color: rgb(255, 255, 255);")
        self.frame_footer.setFrameShape(QFrame.StyledPanel)
        self.frame_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_footer)
        self.horizontalLayout_6.setSpacing(50)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_12 = QLabel(self.frame_footer)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label_12)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.label_13 = QLabel(self.frame_footer)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_6.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_footer)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_6.addWidget(self.label_14)


        self.verticalLayout_3.addWidget(self.frame_footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043f\u0430\u0440\u043e\u043b\u0435\u0439", None))
        self.roll_up_btn.setText("")
        self.exit_btn.setText("")
        self.label_5.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u0445\u0440\u0430\u043d\u0435\u043d\u0438\u044f \u043f\u0430\u0440\u043e\u043b\u0435\u0439", None))
        self.btn_settings.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.btn_pass_reestr.setText("")
#if QT_CONFIG(shortcut)
        self.btn_pass_reestr.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0440\u0435\u0435\u0441\u0442\u0440 \u043f\u0430\u0440\u043e\u043b\u0435\u0439", None))
        self.btn_edit_pass_reestr.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u" \u0440\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.git_btn.setText(QCoreApplication.translate("MainWindow", u"   \u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.key_btn.setText(QCoreApplication.translate("MainWindow", u"   \u041a\u043b\u044e\u0447\u0438               ", None))
        self.db_btn.setText(QCoreApplication.translate("MainWindow", u"   \u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445    ", None))
        self.main_menu_btn_set.setText(QCoreApplication.translate("MainWindow", u"   \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0433\u0438\u0437\u0430\u0446\u0438\u044f ", None))
        self.token_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u043e\u043a\u0435\u043d \u0434\u043b\u044f \u0441\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u0438", None))
        self.label_info_sinc.setText("")
        self.btn_sinc.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447\u0438", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u0414\u043b\u044f \u043f\u0440\u043e\u0432\u0435\u0440\u043a\u0438 \u043a\u043b\u044e\u0447\u0435\u0439 \u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043f\u0440\u0435\u0434\u0432\u0430\u0440\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u043f\u043e\u043b\u043e\u0436\u0438\u0442\u044c \u0438\u0445  \u0432 \u043a\u0430\u0442\u0430\u043b\u043e\u0433 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b (keys). \u041f\u043e\u0441\u043b\u0435 \u0447\u0435\u0433\u043e \u0432\u0435\u0441\u0442\u0438 \u043f"
                        "\u0430\u0440\u043e\u043b\u044c \u0438 \u043d\u0430\u0436\u0430\u0442\u044c \u043a\u043d\u043e\u043f\u0443 \u0441\u0438\u043d\u0445\u0440\u043e\u043d\u0438\u0437\u0430\u0446\u0438\u0438!</span></p></body></html>", None))
        self.edit_pass_key.setText("")
        self.edit_pass_key.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.info_key.setText("")
        self.btn_add_key.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.db_pass_edit.setText("")
        self.db_pass_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f \u043a \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0435\u0439", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c", None))
        self.db_login_edit.setText("")
        self.db_login_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0437\u0434\u0430\u0442\u044c \u0435\u0441\u043b\u0438 \u043d\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.label_info_db.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0440\u0435\u0432\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.go_back_menu_reestr.setText(QCoreApplication.translate("MainWindow", u"   \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0440\u0435\u0432\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.main_menu_page_edit_btn.setText(QCoreApplication.translate("MainWindow", u"  \u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0432\u0435\u0440\u0441\u0438\u044f 1.0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Dorokhinra", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"2022 \u0433\u043e\u0434", None))
    # retranslateUi

