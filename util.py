import psycopg2


def get_connection(user, password, host, db,port):
    try:
        connection = psycopg2.connect(user=user,
                                password=password,
                                host=host,
                                database=db,
                                port=port
                               )
        return connection
    except Exception as e:
        raise(e)


def get_cursor(connection):
    return connection.cursor()