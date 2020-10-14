from util import get_connection, get_cursor
from write import get_insert_query, insert_data


def connect(table_name, dates_with_attributes):
    connection = get_connection('anki_user', 'ankireddy', 'localhost', 'dates', 5432)
    cursor = get_cursor(connection)
    ins_query = get_insert_query(table_name)
    insert_data(connection, cursor, ins_query, dates_with_attributes)
    connection.close()
