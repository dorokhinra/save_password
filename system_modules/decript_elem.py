from PyQt5.QtSql import QSqlQuery

from database.query import query_select_elem_for_decrypt


def decrypt_elem(id, session, auth, decrypt_func):

    query_string = query_select_elem_for_decrypt(id)
    session.open(auth['login'], auth['password'])
    query = QSqlQuery(session)
    query.prepare(query_string)
    query.exec_()
    query.next()
    id_elem = query.value(0)
    login = decrypt_func(query.value(1)).decode()
    password = decrypt_func(query.value(2)).decode()
    description = decrypt_func(query.value(3)).decode()
    create_utc = query.value(4)
    parent_id = query.value(5)
    return {'id': id_elem,  'login': login, 'password': password,
            'description': description, 'create_utc': create_utc, 'parent_id': parent_id}
