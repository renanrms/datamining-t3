from general.logging import logger


def run_sql_script(connection, path):
    with open(path, "r") as file:
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
