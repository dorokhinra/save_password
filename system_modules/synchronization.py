from qt_core import *
import os


class CheckSync:
    def __init__(self):
        path = os.path.abspath(os.getcwd())
        self.path_html = os.path.normpath(os.path.join(path, "html"))
        self.template_danger = os.path.normpath(os.path.join(self.path_html, "infoYa1.html"))
        self.template_succes = os.path.normpath(os.path.join(self.path_html, "info3.html"))

    def check_sync(self, settings, info_widget, style):
        if settings.value('token') is not None:
            info_widget.setStyleSheet(style['success'])
            info_widget.setSource(QtCore.QUrl.fromLocalFile(self.template_succes))
        else:
            info_widget.setStyleSheet(style['danger'])
            info_widget.setSource(QtCore.QUrl.fromLocalFile(self.template_danger))

