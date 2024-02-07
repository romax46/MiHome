import psycopg2
from MiHOme_Web.config import postge_user, postge_pass, postge_server

try:
    connection = psycopg2.connect(
        host=postge_server,
        user=postge_user,
        password=postge_pass,
        database='postgres'
    )
    cursor = connection.cursor()
    cursor.execute("select version();")
    print(f'Server version: {cursor.fetchone()}')
    connection.close()
    print('[INFO] Close session PostgreSQL')

except Exception as _ex:
    print('[INFO] Error with PostgreSQL', _ex)


