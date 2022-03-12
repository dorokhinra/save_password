# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_uiGIisuI.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 738)
        MainWindow.setMinimumSize(QSize(1000, 738))
        MainWindow.setMaximumSize(QSize(1000, 738))
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
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(117, 231, 163, 1), stop:1 rgba(117, 231, 163, 0));")
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
        self.frame_2.setStyleSheet(u"font: 14pt \"MS Shell Dlg 2\";")
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
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.frame_body)

        self.frame_footer = QFrame(self.centralwidget)
        self.frame_footer.setObjectName(u"frame_footer")
        self.frame_footer.setMinimumSize(QSize(0, 40))
        self.frame_footer.setMaximumSize(QSize(16777215, 40))
        self.frame_footer.setStyleSheet(u"background-color: rgba(37, 48, 38, 1)")
        self.frame_footer.setFrameShape(QFrame.StyledPanel)
        self.frame_footer.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_footer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

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
    # retranslateUi

