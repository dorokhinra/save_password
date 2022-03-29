from PyQt5.QtSql import QSqlQuery

from database.query import query_select_elem_for_decrypt


def decrypt_elem(id, session, auth):

    query_string = query_select_elem_for_decrypt(id)
    session.open(auth['login'], auth['password'])
    query = QSqlQuery(session)
    query.prepare(query_string)
    query.exec_()
    query.next()
    id_elem = query.value(0)
    login = query.value(1)
    password = query.value(2)
    description = query.value(3)
    create_utc = query.value(4)
    parent_id = query.value(5)
    return {'id': id_elem,  'login': login, 'password': password,
            'description': description, 'create_utc': create_utc, 'parent_id': parent_id}
