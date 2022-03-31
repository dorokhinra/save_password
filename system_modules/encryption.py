import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


class Encryption():
    def __init__(self, parent):
        self.parent = parent
        app_path = os.path.abspath(os.getcwd())
        folder = "key"
        path = os.path.join(app_path, folder)
        self.path_key = os.path.normpath(os.path.join(path, "genkey.key"))
        self.key = ''

    def check_key(self):
        if os.path.exists(self.path_key):
            self.parent.info_key.setStyleSheet('color: rgb(255, 255, 255);')
            self.parent.info_key.setText('Ключ сучествует, введите пароль!')
        else:
            self.parent.info_key.setStyleSheet('color: rgb(234, 78, 117);')
            self.parent.info_key.setText('Ключ не существует, по нажатию кнопки, будет создан новый ключ!')

    def bush_connect_button(self):
        if self.parent.edit_pass_key.text() != '':
            if not os.path.exists(self.path_key):
                self.create_key()
            self.decrypt_key()
        else:
            self.parent.info_key.setStyleSheet('color: rgb(234, 78, 117);')
            self.parent.info_key.setText('Заполните все поля!')

    def create_key(self):
        # Создаем ключ и сохраняем его в файл
        password = self.parent.edit_pass_key.text()
        key_gen = Fernet.generate_key()
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                         length=32,
                         salt=salt,
                         iterations=100000,
                         )
        key_pass = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        f = Fernet(key_pass)
        token = f.encrypt(key_gen)
        with open(self.path_key, 'wb') as key_file:
            key_file.write(token)

    def decrypt_key(self):
        password = self.parent.edit_pass_key.text()
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                         length=32,
                         salt=salt,
                         iterations=100000,
                         )
        key_pass = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        f = Fernet(key_pass)
        with open(self.path_key, 'rb') as file:
            encrypt_key = file.read()
        try:
            self.key = f.decrypt(encrypt_key)

        except:
            self.parent.info_key.setStyleSheet('color: rgb(234, 78, 117);')
            self.parent.info_key.setText('Не верный пароль!')

