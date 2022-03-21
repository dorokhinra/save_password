import os
from qt_core import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from database.query import create_tables


class DbSession(object):

    def __init__(self):
        app_path = os.path.abspath(os.getcwd())
        folder = "database/db_file"
        path = os.path.join(app_path, folder)
        self.db_path = os.path.normpath(os.path.join(path, "password_store.sqlite"))
        self.session = self.session_query()

    def session_query(self):
        session = QSqlDatabase.addDatabase("QSQLITE")
        session.setDatabaseName(self.db_path)
        return QSqlDatabase.database(open=False)

    def create_table(self, session):
        session.open('test', 'Win2018!')
        self.query = QSqlQuery(session)
        query_string = create_tables()['categories']
        self.query.prepare(query_string)
        self.query.exec_()
        query_string = create_tables()['password_store']
        self.query.prepare(query_string)
        self.query.exec_()

