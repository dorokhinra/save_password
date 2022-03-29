import uuid
import datetime
def create_tables():
    password_store = """
        CREATE TABLE IF NOT EXISTS password_store (
    	id TEXT,
    	login TEXT,
    	password TEXT,
    	description TEXT,
    	create_utc TEXT,
    	parent_id TEXT
    );
    """
    categories = """
    CREATE TABLE IF NOT EXISTS categories (
    	id TEXT,
    	parent_id TEXT,
    	name_category TEXT,
    	create_utc TEXT
    );
    """
    return {'password_store': password_store, 'categories': categories }

# def create_tables():
#     return """
#     CREATE TABLE IF NOT EXISTS password_store (
#     	id TEXT,
#     	login TEXT,
#     	password TEXT,
#     	description TEXT,
#     	create_utc TEXT,
#     	parent_id TEXT);
#
#     CREATE TABLE IF NOT EXISTS categories (
#     	id TEXT,
#     	parent_id TEXT,
#     	name_category TEXT,
#     	create_utc TEXT
#     );
#     """

def query_data():
    query_all_categories = """
    SELECT * FROM categories;
    """
    return {'query_all_categories': query_all_categories}


def query_insert_cat(data):
    return f"""
    INSERT INTO categories (id, parent_id, name_category, create_utc)
    VALUES ('{uuid.uuid4()}', '{data['parent_id']}', '{data['name']}', '{datetime.datetime.now()}');
    """


def query_insert_elem(data):
    return f"""
    INSERT INTO password_store (id, login, password, description, create_utc, parent_id)
    VALUES ('{uuid.uuid4()}', '{data['login']}', '{data['password']}', '{data['description']}', '{datetime.datetime.now()}', '{data['parent_id']}');
    """


def query_delete_category(id):
    return f"""
    DELETE FROM categories WHERE id = '{id}';
    """

def query_delete_element_in_cat(id):
    return f"""
       DELETE FROM password_store WHERE parent_id = '{id}';
       """

def query_update_elem(data):
    return f"""
    UPDATE password_store SET login = '{data['login']}', password = '{data['password']}', description = '{data['description']}', create_utc = '{datetime.datetime.now()}' WHERE id = '{data['id']}';
    """

def query_delet_elem(id):
    return f"""
         DELETE FROM password_store WHERE id = '{id}';
         """

def query_change_category_on_double_click(id, data):
    return f"""
    UPDATE categories SET name_category = '{data}', create_utc = '{datetime.datetime.now()}' WHERE id = '{id}';
    """

def query_select_elem_for_decrypt(id):
    return f"""
    SELECT * FROM password_store WHERE id = '{id}';
    """