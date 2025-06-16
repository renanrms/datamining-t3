import os
import json

from psycopg2 import sql
from psycopg2.extras import execute_batch
from datetime import datetime

from general.logging import logger
from database.connection import connection
from database.create_database_schema import create_database_schema


def convert_timestamp(timestamp):
    """Converte timestamp em milissegundos para objeto datetime"""
    try:
        return datetime.fromtimestamp(int(timestamp)/1000)
    except:
        return None


def process_json_file(file_path, connection):
    """Processa um arquivo JSON e insere os dados no banco"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        # Prepara os dados para inserção
        records = []
        for entry in data:
            try:
                # Converte coordenadas para formato numérico (substitui , por .)
                lat = float(entry['latitude'].replace(',', '.'))
                lon = float(entry['longitude'].replace(',', '.'))

                # Converte timestamps
                dt = convert_timestamp(entry['datahora'])
                dt_envio = convert_timestamp(entry.get('datahoraenvio'))
                dt_servidor = convert_timestamp(entry.get('datahoraservidor'))

                if not dt:  # Se não conseguiu converter a data principal, ignora o registro
                    continue

                records.append((
                    entry['ordem'],
                    lon, lat,  # ST_MakePoint recebe longitude primeiro
                    dt,
                    float(entry['velocidade']
                          ) if entry['velocidade'] else None,
                    entry['linha'],
                    dt_envio,
                    dt_servidor
                ))
            except Exception as e:
                logger.warning(
                    f"Erro no registro do arquivo {file_path}: {str(e)}")
                continue

        # Insere em lote usando execute_batch para melhor performance
        if records:
            cursor = connection.cursor()
            query = sql.SQL('''
            INSERT INTO tracking (
                ordem, geom, datahora, velocidade,
                linha, datahoraenvio, datahoraservidor
            ) VALUES (
                %s, ST_SetSRID(ST_MakePoint(%s, %s), 4326), %s, %s, %s, %s, %s
            )
            ''')

            execute_batch(cursor, query, records)
            connection.commit()

            return len(records)
        return 0

    except Exception as e:
        connection.rollback()
        logger.error(f"Erro ao processar {file_path}: {str(e)}")
        return 0


def import_all_data(connection, input_folder='../../input/train'):
    """Importa todos os dados das pastas diárias para o banco de dados"""
    total_files = 0
    total_records = 0

    try:
        # Percorre todas as pastas diárias
        for day_folder in sorted(os.listdir(input_folder)):
            day_path = os.path.join(input_folder, day_folder)

            if not os.path.isdir(day_path):
                continue

            logger.info(f"Processando dia: {day_folder}")

            # Processa cada arquivo JSON na pasta do dia
            for json_file in sorted(os.listdir(day_path)):
                if json_file.endswith('.json'):
                    file_path = os.path.join(day_path, json_file)
                    records_added = process_json_file(file_path, connection)

                    total_files += 1
                    total_records += records_added

                    if records_added > 0:
                        logger.info(
                            f"  {json_file}: {records_added} registros adicionados")

    except Exception as e:
        logger.error(f"Erro durante a importação: {str(e)}")
        raise
    finally:
        if connection:
            connection.close()
        logger.info(
            f"\nImportação concluída! Total: {total_files} arquivos processados, {total_records} registros inseridos.")


if __name__ == '__main__':

    # Criar o schema do banco de dados
    create_database_schema(connection)

    # Importar todos os dados
    import_all_data(connection)
