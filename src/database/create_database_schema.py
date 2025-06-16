from general.logging import logger


def create_database_schema(connection):
    """Cria a tabela e extensões necessárias no PostgreSQL"""

    with open("../sql/db_init.sql", "r") as file:
        sql = file.read()
        cursor = connection.cursor()
        for command in sql.split(';'):
            if command.strip():
                try:
                    cursor.execute(command)
                    connection.commit()
                except Exception as e:
                    logger.error("Erro ao executar comando:")
                    logger.error(command)
                    logger.error(e)
                    connection.rollback()
                    break
