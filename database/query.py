

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