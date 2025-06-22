from database.run_sql_script import run_sql_script


def create_database_schema(connection):
    """Cria a tabela e extensões necessárias no PostgreSQL"""

    run_sql_script(connection, "../sql/202506152325_db_init.sql")
