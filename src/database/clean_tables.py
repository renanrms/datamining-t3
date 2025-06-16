# Função para truncar a tabela load
def clean_tables(connection):
    cursor = connection.cursor()
    cursor.execute("TRUNCATE TABLE tracking")
    connection.commit()
