# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uiiEtlWc.ui'
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
        self.frame_32 = QFrame(self.page_1)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setMinimumSize(QSize(0, 40))
        self.frame_32.setMaximumSize(QSize(16777215, 227))
        self.frame_32.setStyleSheet(u"#frame_32{\n"
"	background-image: url(:/images/fon_baner.png);\n"
"}")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_32)
        self.verticalLayout_36.setSpacing(0)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.frame_31 = QFrame(self.frame_32)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMinimumSize(QSize(0, 40))
        self.frame_31.setStyleSheet(u"#frame_31{\n"
"	background-color: rgba(31, 31, 31, 0.9);\n"
"}")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_31)
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_31)
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


        self.verticalLayout_35.addWidget(self.frame)


        self.verticalLayout_36.addWidget(self.frame_31)


        self.verticalLayout_2.addWidget(self.frame_32)

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

        self.frame_get_frame = QFrame(self.frame_7)
        self.frame_get_frame.setObjectName(u"frame_get_frame")
        self.frame_get_frame.setMaximumSize(QSize(16777215, 60))
        self.frame_get_frame.setStyleSheet(u"#frame_get_frame {\n"
"	border:none;\n"
"	background-color: rgba(255, 255, 255, 0.0);\n"
"}")
        self.frame_get_frame.setFrameShape(QFrame.StyledPanel)
        self.frame_get_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_get_frame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.get_code_btn = QPushButton(self.frame_get_frame)
        self.get_code_btn.setObjectName(u"get_code_btn")
        self.get_code_btn.setMinimumSize(QSize(200, 40))
        self.get_code_btn.setMaximumSize(QSize(16777215, 40))
        self.get_code_btn.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_11.addWidget(self.get_code_btn)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)


        self.verticalLayout_14.addWidget(self.frame_get_frame)

        self.input_code_frame = QFrame(self.frame_7)
        self.input_code_frame.setObjectName(u"input_code_frame")
        self.input_code_frame.setMaximumSize(QSize(16777215, 0))
        self.input_code_frame.setStyleSheet(u"	border:none;\n"
"	background-color: rgba(255, 255, 255, 0.0);")
        self.input_code_frame.setFrameShape(QFrame.StyledPanel)
        self.input_code_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.input_code_frame)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.edit_code = QLineEdit(self.input_code_frame)
        self.edit_code.setObjectName(u"edit_code")
        self.edit_code.setMinimumSize(QSize(0, 40))
        self.edit_code.setStyleSheet(u"QLineEdit {\n"
"border-radius: 10px;\n"
"background-color: rgba(36, 36, 36, 0.9);\n"
"border: 3px   solid rgba(37, 48, 38, 1);	 \n"
"padding: 5px;\n"
"}")

        self.verticalLayout_26.addWidget(self.edit_code)

        self.frame_24 = QFrame(self.input_code_frame)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)

        self.input_code_btn = QPushButton(self.frame_24)
        self.input_code_btn.setObjectName(u"input_code_btn")
        self.input_code_btn.setMinimumSize(QSize(200, 40))
        self.input_code_btn.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_12.addWidget(self.input_code_btn)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_10)


        self.verticalLayout_26.addWidget(self.frame_24)


        self.verticalLayout_14.addWidget(self.input_code_frame)

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
        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_10, 4, 0, 1, 2)

        self.btn_push = QPushButton(self.frame_8)
        self.btn_push.setObjectName(u"btn_push")
        self.btn_push.setMinimumSize(QSize(0, 40))
        self.btn_push.setMaximumSize(QSize(200, 16777215))
        self.btn_push.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_2.addWidget(self.btn_push, 1, 0, 1, 1)

        self.btn_update = QPushButton(self.frame_8)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setMinimumSize(QSize(100, 40))
        self.btn_update.setMaximumSize(QSize(200, 16777215))
        self.btn_update.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_2.addWidget(self.btn_update, 1, 1, 1, 1)

        self.frame_22 = QFrame(self.frame_8)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(0, 40))
        self.frame_22.setMaximumSize(QSize(16777215, 150))
        self.frame_22.setStyleSheet(u"#frame_22 {\n"
"border:none;\n"
"	background-color: rgba(255, 255, 255, 0.0);\n"
"}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_22)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.info_ya_api = QTextBrowser(self.frame_22)
        self.info_ya_api.setObjectName(u"info_ya_api")
        self.info_ya_api.setMaximumSize(QSize(16777215, 400))
        self.info_ya_api.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(203, 206, 65, 1), stop:1 rgba(203, 206, 65, 0));\n"
"border: none;\n"
"border-radius: 25px;\n"
"padding: 15 5 5 5px;")

        self.verticalLayout_25.addWidget(self.info_ya_api)


        self.gridLayout_2.addWidget(self.frame_22, 3, 0, 1, 2)


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
        self.textEdit.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(203, 206, 65, 1), stop:1 rgba(203, 206, 65, 0));\n"
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

        self.frame_db_pass_info = QFrame(self.frame_6)
        self.frame_db_pass_info.setObjectName(u"frame_db_pass_info")
        self.frame_db_pass_info.setMinimumSize(QSize(0, 40))
        self.frame_db_pass_info.setMaximumSize(QSize(16777215, 100))
        self.frame_db_pass_info.setStyleSheet(u"border:none;\n"
"background-color: rgba(255, 255, 255, 0.0);")
        self.frame_db_pass_info.setFrameShape(QFrame.StyledPanel)
        self.frame_db_pass_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_db_pass_info)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.db_pass_info = QTextBrowser(self.frame_db_pass_info)
        self.db_pass_info.setObjectName(u"db_pass_info")
        self.db_pass_info.setMaximumSize(QSize(400, 16777215))
        self.db_pass_info.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(203, 206, 65, 1), stop:1 rgba(203, 206, 65, 0));\n"
"border: none;\n"
"border-radius: 25px;\n"
"padding: 15 5 5 5px;")

        self.horizontalLayout_10.addWidget(self.db_pass_info)


        self.gridLayout.addWidget(self.frame_db_pass_info, 9, 0, 1, 3)

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

        self.label_info_db = QLabel(self.frame_6)
        self.label_info_db.setObjectName(u"label_info_db")
        self.label_info_db.setMaximumSize(QSize(16777215, 25))
        self.label_info_db.setStyleSheet(u"color: rgb(234, 78, 117);\n"
"background-color: rgba(255, 255, 255, 0.0);")

        self.gridLayout.addWidget(self.label_info_db, 6, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_8, 10, 0, 1, 3)

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

        self.frame_21 = QFrame(self.frame_6)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setStyleSheet(u"#frame_21 {\n"
"border: none;\n"
"	background-color: rgba(255, 255, 255, 0.0);\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(self.frame_21)
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

        self.horizontalLayout_9.addWidget(self.pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)


        self.gridLayout.addWidget(self.frame_21, 7, 0, 1, 3)

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

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_9, 0, 0, 1, 3)

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_16, 2, 0, 1, 3)

        self.verticalSpacer_17 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.verticalSpacer_17, 8, 0, 1, 3)


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
        self.frame_12.setStyleSheet(u"#frame_12 {\n"
"	background-image: url(:/images/fon_menu.png);\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_12)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.frame_12)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setMinimumSize(QSize(0, 100))
        self.frame_26.setStyleSheet(u"#frame_26 {\n"
"background-color: rgba(37, 48, 38, 0.8);\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_26)
        self.verticalLayout_29.setSpacing(2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.frame_26)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(0, 40))
        self.frame_25.setStyleSheet(u"#frame_25 {\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(164, 16, 131, 1), stop:1 rgba(164, 16, 131, 0));\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_25)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_17 = QLabel(self.frame_25)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(0, 40))
        self.label_17.setStyleSheet(u"font: 12pt \"Sans Serif\";\n"
"border-bottom: 2px   solid rgb(184, 184, 184);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(117, 231, 163, 1), stop:1 rgba(117, 231, 163, 0));\n"
"border-radius: 5px;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_17)

        self.treeView_2 = QTreeView(self.frame_25)
        self.treeView_2.setObjectName(u"treeView_2")
        self.treeView_2.setStyleSheet(u"QTreeView {\n"
"background-color: rgba(193, 193, 193, 0.1);\n"
"        }  \n"
"/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(45, 45, 68);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {	\n"
"	background-color: rgb(80, 80, 122);\n"
"	min-height: 30px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::handle:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::sub-line:vertical:"
                        "pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"	border: none;\n"
"	background-color: rgb(59, 59, 90);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::add-line:vertical:hover {	\n"
"	background-color: rgb(255, 0, 127);\n"
"}\n"
"QScrollBar::add-line:vertical:pressed {	\n"
"	background-color: rgb(185, 0, 92);\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"	background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"/* HORIZONTAL SCROLLBAR - HOMEWORK */\n"
"QScrollBar:horizontal {\n"
"   \n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    \n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    \n"
"}\n"
"QScroll"
                        "Bar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"\n"
"}    ")

        self.verticalLayout_28.addWidget(self.treeView_2)

        self.main_menu_page_edit_btn = QPushButton(self.frame_25)
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

        self.verticalLayout_28.addWidget(self.main_menu_page_edit_btn)


        self.verticalLayout_29.addWidget(self.frame_25)


        self.verticalLayout_18.addWidget(self.frame_26)


        self.horizontalLayout_8.addWidget(self.frame_12)

        self.horizontalSpacer_11 = QSpacerItem(20, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_11)

        self.frame_13 = QFrame(self.page_edit)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setStyleSheet(u"#frame_13{	\n"
"	background-image: url(:/images/fon_table.png);\n"
"	border-radius: 25px;\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_13)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setStyleSheet(u"#frame_23 {\n"
"	background-color: rgba(65, 65, 65, 0.8);\n"
"border-radius: 25px;\n"
"}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_23)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_23)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 40))
        self.label_18.setMaximumSize(QSize(16777215, 40))
        self.label_18.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(117, 231, 163, 1), stop:1 rgba(117, 231, 163, 0));\n"
"font: 12pt \"Sans Serif\";\n"
"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;\n"
"")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_27.addWidget(self.label_18)

        self.frame_14 = QFrame(self.frame_23)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"#frame_14{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(91, 193, 200, 1), stop:1 rgba(91, 193, 200, 0));\n"
"border-bottom-left-radius: 20px;\n"
"border-bottom-right-radius: 20px;\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_14)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, -1)
        self.frame_27 = QFrame(self.frame_14)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setMinimumSize(QSize(0, 50))
        self.frame_27.setMaximumSize(QSize(16777215, 50))
        self.frame_27.setStyleSheet(u"background-color: rgba(37, 48, 38, 0.8);")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_27)
        self.verticalLayout_31.setSpacing(0)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.element_name = QLabel(self.frame_27)
        self.element_name.setObjectName(u"element_name")
        self.element_name.setMinimumSize(QSize(0, 50))
        self.element_name.setStyleSheet(u"background-color: rgba(37, 48, 38, 0.6);\n"
"font: 11pt \"Sans Serif\";\n"
"")
        self.element_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_31.addWidget(self.element_name)


        self.verticalLayout_30.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_14)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"#frame_28 {\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(117, 231, 163, 1), stop:1 rgba(117, 231, 163, 0));\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_28)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_15 = QLabel(self.frame_28)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 40))
        self.label_15.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.0);\n"
"font: 12pt \"Sans Serif\";\n"
"text-decoration: underline;")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.label_15)

        self.frame_29 = QFrame(self.frame_28)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setMinimumSize(QSize(0, 70))
        self.frame_29.setMaximumSize(QSize(16777215, 70))
        self.frame_29.setStyleSheet(u"font: 11pt \"Sans Serif\";\n"
"background-color: rgba(255, 255, 255, 0.0);")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)

        self.elemen_radio = QRadioButton(self.frame_29)
        self.elemen_radio.setObjectName(u"elemen_radio")
        self.elemen_radio.setStyleSheet(u"QRadioButton {\n"
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

        self.horizontalLayout_13.addWidget(self.elemen_radio)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_15)

        self.cotegori_radio = QRadioButton(self.frame_29)
        self.cotegori_radio.setObjectName(u"cotegori_radio")
        self.cotegori_radio.setStyleSheet(u"QRadioButton {\n"
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
        self.cotegori_radio.setChecked(True)

        self.horizontalLayout_13.addWidget(self.cotegori_radio)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)


        self.verticalLayout_32.addWidget(self.frame_29)

        self.frame_30 = QFrame(self.frame_28)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"#frame_30{\n"
"	background-color: rgba(255, 255, 255, 0.0);\n"
"}")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_30)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(40, 11, 40, 11)
        self.frame_name_category_edit = QFrame(self.frame_30)
        self.frame_name_category_edit.setObjectName(u"frame_name_category_edit")
        self.frame_name_category_edit.setMaximumSize(QSize(16777215, 100))
        self.frame_name_category_edit.setStyleSheet(u"#frame_name_category_edit{\n"
"	background-color: rgba(255, 255, 255, 0.0);\n"
"}")
        self.frame_name_category_edit.setFrameShape(QFrame.StyledPanel)
        self.frame_name_category_edit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_name_category_edit)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.edit_name_category = QLineEdit(self.frame_name_category_edit)
        self.edit_name_category.setObjectName(u"edit_name_category")
        self.edit_name_category.setMinimumSize(QSize(0, 40))
        self.edit_name_category.setStyleSheet(u"QLineEdit {\n"
"border-radius: 10px;\n"
"background-color: rgba(36, 36, 36, 0.9);\n"
"border: 3px   solid rgba(37, 48, 38, 1);	 \n"
"padding: 5px;\n"
"}")

        self.verticalLayout_34.addWidget(self.edit_name_category)


        self.verticalLayout_33.addWidget(self.frame_name_category_edit)

        self.frame_element_edit = QFrame(self.frame_30)
        self.frame_element_edit.setObjectName(u"frame_element_edit")
        self.frame_element_edit.setMaximumSize(QSize(16777215, 250))
        self.frame_element_edit.setStyleSheet(u"#frame_element_edit{\n"
"	background-color: rgba(255, 255, 255, 0.0);\n"
"}\n"
"QLineEdit {\n"
"border-radius: 10px;\n"
"background-color: rgba(36, 36, 36, 0.9);\n"
"border: 3px   solid rgba(37, 48, 38, 1);	 \n"
"padding: 5px;\n"
"}")
        self.frame_element_edit.setFrameShape(QFrame.StyledPanel)
        self.frame_element_edit.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_element_edit)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(25)
        self.edit_password = QLineEdit(self.frame_element_edit)
        self.edit_password.setObjectName(u"edit_password")
        self.edit_password.setMinimumSize(QSize(0, 40))
        self.edit_password.setEchoMode(QLineEdit.Password)

        self.gridLayout_4.addWidget(self.edit_password, 0, 1, 1, 1)

        self.edit_login = QLineEdit(self.frame_element_edit)
        self.edit_login.setObjectName(u"edit_login")
        self.edit_login.setMinimumSize(QSize(0, 40))

        self.gridLayout_4.addWidget(self.edit_login, 0, 0, 1, 1)

        self.description_edit = QTextEdit(self.frame_element_edit)
        self.description_edit.setObjectName(u"description_edit")
        self.description_edit.setStyleSheet(u"border-radius: 10px;\n"
"background-color: rgba(36, 36, 36, 0.9);\n"
"border: 3px   solid rgba(37, 48, 38, 1);	 \n"
"padding: 5px;")

        self.gridLayout_4.addWidget(self.description_edit, 2, 0, 1, 2)


        self.verticalLayout_33.addWidget(self.frame_element_edit)

        self.info_for_edit_elements = QLabel(self.frame_30)
        self.info_for_edit_elements.setObjectName(u"info_for_edit_elements")
        self.info_for_edit_elements.setStyleSheet(u"background-color: rgba(247, 247, 247, 0.0);\n"
"color: rgb(232, 77, 0);")
        self.info_for_edit_elements.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.info_for_edit_elements)

        self.label_success_info = QLabel(self.frame_30)
        self.label_success_info.setObjectName(u"label_success_info")
        self.label_success_info.setStyleSheet(u"background-color: rgba(247, 247, 247, 0.0);\n"
"color: rgb(0, 170, 0);")
        self.label_success_info.setTextFormat(Qt.PlainText)
        self.label_success_info.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.label_success_info)

        self.confitm_edit_reestr_frame = QFrame(self.frame_30)
        self.confitm_edit_reestr_frame.setObjectName(u"confitm_edit_reestr_frame")
        self.confitm_edit_reestr_frame.setMinimumSize(QSize(0, 0))
        self.confitm_edit_reestr_frame.setMaximumSize(QSize(16777215, 60))
        self.confitm_edit_reestr_frame.setStyleSheet(u"#confitm_edit_reestr_frame{\n"
"	background-color: rgba(255, 255, 255, 0.0);\n"
"}")
        self.confitm_edit_reestr_frame.setFrameShape(QFrame.StyledPanel)
        self.confitm_edit_reestr_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.confitm_edit_reestr_frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_16)

        self.confitm_edit_reestr_btn = QPushButton(self.confitm_edit_reestr_frame)
        self.confitm_edit_reestr_btn.setObjectName(u"confitm_edit_reestr_btn")
        self.confitm_edit_reestr_btn.setMinimumSize(QSize(200, 40))
        self.confitm_edit_reestr_btn.setStyleSheet(u"QPushButton{\n"
"	font: 12pt \"Sans Serif\";\n"
"	background-color: rgba(37, 48, 38, 0.8);\n"
"\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgba(37, 48, 38, 0.6);\n"
"border: 3px   solid rgba(195, 195, 195, 0.7);\n"
"	 \n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: rgba(216, 216, 216, 0.2);\n"
"}")

        self.horizontalLayout_14.addWidget(self.confitm_edit_reestr_btn)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_17)


        self.verticalLayout_33.addWidget(self.confitm_edit_reestr_frame)


        self.verticalLayout_32.addWidget(self.frame_30)


        self.verticalLayout_30.addWidget(self.frame_28)


        self.verticalLayout_27.addWidget(self.frame_14)


        self.verticalLayout_17.addWidget(self.frame_23)


        self.horizontalLayout_8.addWidget(self.frame_13)

        self.horizontalSpacer_12 = QSpacerItem(15, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)

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

        self.stackedWidget.setCurrentIndex(3)
        self.stackedWidget_2.setCurrentIndex(2)


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
        self.get_code_btn.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c \u043a\u043e\u0434", None))
        self.edit_code.setText("")
        self.edit_code.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043a\u043e\u0434 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.input_code_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043f\u0440\u0430\u0432\u0438\u0442\u044c", None))
        self.label_info_sinc.setText("")
        self.btn_push.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043d\u0430 \u042f.\u0414\u0438\u0441\u043a", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
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
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f \u043a \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u044e\u0449\u0435\u0439", None))
        self.db_pass_info.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.db_pass_edit.setText("")
        self.db_pass_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_info_db.setText("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0437\u0434\u0430\u0442\u044c \u0435\u0441\u043b\u0438 \u043d\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043d\u044f\u0442\u044c", None))
        self.db_login_edit.setText("")
        self.db_login_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0431\u0430\u0437\u044b \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0440\u0435\u0432\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.go_back_menu_reestr.setText(QCoreApplication.translate("MainWindow", u"   \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0440\u0435\u0432\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.main_menu_page_edit_btn.setText(QCoreApplication.translate("MainWindow", u"  \u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0434\u0430\u043a\u0442\u043e\u0440 \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u0430", None))
        self.element_name.setText(QCoreApplication.translate("MainWindow", u"\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c:", None))
        self.elemen_radio.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043b\u0435\u043c\u0435\u043d\u0442", None))
        self.cotegori_radio.setText(QCoreApplication.translate("MainWindow", u"\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e", None))
        self.edit_name_category.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.edit_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.edit_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.description_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.info_for_edit_elements.setText("")
        self.label_success_info.setText("")
        self.confitm_edit_reestr_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0432\u0435\u0440\u0441\u0438\u044f 1.0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Dorokhinra", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"2022 \u0433\u043e\u0434", None))
    # retranslateUi

