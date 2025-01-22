import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


def kill_queries():
    host = os.getenv("DB_HOST")
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    database = os.getenv("DB_NAME")

    connection = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )

    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT id
            FROM information_schema.processlist
            WHERE TIME > 100 AND STATE = 'executing' AND USER <> 'rdsrepladmin' AND command <> 'SLEEP';
        """
        )

        queries_to_kill = cursor.fetchall()

        if not queries_to_kill:
            print("Não há consultas para matar.")
        else:
            for (query_id, ) in queries_to_kill:
                print(f"Mata consulta com ID: {query_id}")
                cursor.callproc(
                    "mysql.rds_kill_query", [query_id]
                )

    except mysql.connector.Error as err:
        print(f"Erro: {err}")

    finally:
        cursor.close()
        connection.close()


kill_queries()
