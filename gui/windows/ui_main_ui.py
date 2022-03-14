# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uihMoMWU.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

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
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stackedWidget_2 = QStackedWidget(self.frame_4)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"background-color: rgba(195, 195, 195, 0.3);")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_9 = QVBoxLayout(self.page_4)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_10)

        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_10 = QVBoxLayout(self.page_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_11)

        self.stackedWidget_2.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_11 = QVBoxLayout(self.page_6)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_8 = QLabel(self.page_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_8)

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

        self.stackedWidget.setCurrentIndex(2)
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
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0445\u0440\u043e\u043d\u0433\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u044e\u0447\u0438", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u0440\u0435\u0432\u043e \u044d\u043b\u0435\u043c\u0435\u043d\u0442\u043e\u0432", None))
        self.go_back_menu_reestr.setText(QCoreApplication.translate("MainWindow", u"   \u0433\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0432\u0435\u0440\u0441\u0438\u044f 1.0", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Dorokhinra", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"2022 \u0433\u043e\u0434", None))
    # retranslateUi

