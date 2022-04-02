from qt_core import *
import os
import yadisk
import webbrowser
import datetime


class CheckSync:
    def __init__(self, settings, parent, style):
        self.path = os.path.abspath(os.getcwd())
        self.path_html = os.path.normpath(os.path.join(self.path, "html"))
        self.template_danger = os.path.normpath(os.path.join(self.path_html, "infoYa1.html"))
        self.template_succes = os.path.normpath(os.path.join(self.path_html, "info3.html"))
        self.template_succes_update = os.path.normpath(os.path.join(self.path_html, "infoYa4.html"))
        self.template_danger_2 = os.path.normpath(os.path.join(self.path_html, "info4.html"))
        self.template_error = os.path.normpath(os.path.join(self.path_html, "infoYa2.html"))
        self.template_error_2 = os.path.normpath(os.path.join(self.path_html, "infoYa3.html"))
        self.template_danger_db = os.path.normpath(os.path.join(self.path_html, "info2.html"))
        self.template_danger_3 = os.path.normpath(os.path.join(self.path_html, "infoYa5.html"))
        self.template_danger_4 = os.path.normpath(os.path.join(self.path_html, "infoYa6.html"))

        folder = "database/db_file"
        path = os.path.join(self.path, folder)
        self.path_db = os.path.normpath(os.path.join(path, "password_store.sqlite"))
        self.y = yadisk.YaDisk("e4b953a1900241a99dad6416dc0c0218", "a74315e22a73436683986016c1ae7c57")
        self.parent = parent
        self.settings = settings
        self.style = style

    def get_token(self):
        url = self.y.get_code_url()
        webbrowser.open(url)
        self.animation_check_code()
        self.animation_get_code_btn()

    def input_code(self):
        if self.parent.edit_code.text() != '':
            code = self.parent.edit_code.text()
            try:
                response = self.y.get_token(code)
                self.y.token = response.access_token
                if self.y.check_token():
                    self.parent.info_ya_api.setStyleSheet(self.style['success'])
                    self.parent.info_ya_api.setSource(QtCore.QUrl.fromLocalFile(self.template_succes))
                    self.animation_check_code()
                    self.parent.btn_push.setEnabled(True)
                    self.parent.btn_update.setEnabled(True)
                    self.settings.setValue('token', self.y.token)
                else:
                    self.parent.info_ya_api.setStyleSheet(self.style['error'])
                    self.parent.info_ya_api.setSource(QtCore.QUrl.fromLocalFile(self.template_error))
            except yadisk.exceptions.BadRequestError:
                self.parent.info_ya_api.setStyleSheet(self.style['error'])
                self.parent.info_ya_api.setSource(QtCore.QUrl.fromLocalFile(self.template_error))
        else:
            self.parent.info_ya_api.setStyleSheet(self.style['danger'])
            self.parent.info_ya_api.setSource(QtCore.QUrl.fromLocalFile(self.template_danger_2))

    def save_disk(self):
        if os.path.exists(self.path_db):
            try:
                dir_name = self.check_YaDisk_file_and_dir()['dirname']
                if dir_name == '':
                    self.y.mkdir("disk:/Приложения/store")
                # print(datetime.datetime.now())
                self.y.upload(self.path_db, f"disk:/Приложения/store/{datetime.datetime.now()}")
                self.parent.info_ya_api.setStyleSheet(self.style['success'])
                self.parent.info_ya_api.setSource(QtCore.QUrl.fromLocalFile(self.template_succes_update))
            except yadisk.exceptions.ForbiddenError:
                self.parent.info_ya_api.setStyleSheet(self.style['danger'])
                self.parent.info_ya_api.setSource(QtCore.QUrl.fromLocalFile(self.template_danger_3))

        else:
            self.parent.info_ya_api.setStyleSheet(self.style['danger'])
            self.parent.info_ya_api.setSource(QtCore.QUrl.fromLocalFile(self.template_danger_db))

    def update_db_to_Ya_disk(self):
        list_file = self.check_YaDisk_file_and_dir()['list_file']
        if len(list_file) != 0:
            try:
                self.y.download(f'disk:/Приложения/store/{list_file[-1]}', self.path_db)
                self.parent.info_ya_api.setStyleSheet(self.style['success'])
                self.parent.info_ya_api.setSource(QtCore.QUrl.fromLocalFile(self.template_succes_update))
            except yadisk.exceptions.ForbiddenError:
                self.parent.info_ya_api.setStyleSheet(self.style['danger'])
                self.parent.info_ya_api.setSource(QtCore.QUrl.fromLocalFile(self.template_danger_3))
        else:
            self.parent.info_ya_api.setStyleSheet(self.style['danger'])
            self.parent.info_ya_api.setSource(QtCore.QUrl.fromLocalFile(self.template_danger_4))

    def check_sync(self):
        if self.settings.value('token') is not None:
            self.y.token = self.settings.value('token')
            if self.y.check_token():
                self.parent.frame_get_frame.setMaximumHeight(0)
                self.parent.info_ya_api.setStyleSheet(self.style['success'])
                self.parent.info_ya_api.setSource(QtCore.QUrl.fromLocalFile(self.template_succes))
            else:
                self.parent.btn_push.setEnabled(False)
                self.parent.btn_update.setEnabled(False)
                self.parent.info_ya_api.setStyleSheet(self.style['error'])
                self.parent.info_ya_api.setSource(QtCore.QUrl.fromLocalFile(self.template_error_2))
        else:
            self.parent.btn_push.setEnabled(False)
            self.parent.btn_update.setEnabled(False)
            self.parent.info_ya_api.setStyleSheet(self.style['danger'])
            self.parent.info_ya_api.setSource(QtCore.QUrl.fromLocalFile(self.template_danger))

    def animation_check_code(self):
        input_cod_frame = self.parent.input_code_frame.height()
        width = 0
        if input_cod_frame == 0:
            width = 120
        # Start animation
        self.animation = QPropertyAnimation(self.parent.input_code_frame, b"maximumHeight")
        self.animation.setStartValue(input_cod_frame)
        self.animation.setEndValue(width)
        self.animation.setDuration(700)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.start()

    def animation_get_code_btn(self):
        get_frame_animation = self.parent.frame_get_frame.height()
        height = 0
        if get_frame_animation == 0:
            height = 60
            # Start animation
        self.animation_2 = QPropertyAnimation(self.parent.frame_get_frame, b"maximumHeight")
        self.animation_2.setStartValue(get_frame_animation)
        self.animation_2.setEndValue(height)
        self.animation_2.setDuration(700)
        self.animation_2.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation_2.start()

    def check_YaDisk_file_and_dir(self):
        store = list(self.y.listdir('disk:/Приложения/'))
        dir_name = ''
        list_file = []
        for name in store:
            if name['name'] == 'store':
                dir_name = name['name']
                list_file = list(self.y.listdir('disk:/Приложения/store/'))
                if len(list_file) != 0:
                   list_file = sorted([dict_file_name['name'] for dict_file_name in list_file])

        return {'dirname': dir_name, 'list_file': list_file}


# if __name__ == '__main__':
#     CheckSync().check_token()