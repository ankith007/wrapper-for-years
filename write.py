def get_insert_query(table_name):
    print(2)
    column_names = "DATES"
    value_place_holders = "%s"
    query = (f"""INSERT INTO {table_name}
                 ({column_names})
                 VALUES
                 ({value_place_holders})""")
    return query


def insert_data(connection, cursor, query, dates_with_attributes):
    cursor.executemany(query, dates_with_attributes)
    connection.commit()
