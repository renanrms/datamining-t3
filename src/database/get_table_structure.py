import pandas as pd

from database.engine import engine


def get_table_structure():
    query = """
    SELECT
        a.attname AS column_name,
        pg_catalog.format_type(a.atttypid, a.atttypmod) AS data_type,
        CASE WHEN a.attnotnull THEN 'NOT NULL' ELSE 'NULL' END AS nullable
    FROM
        pg_catalog.pg_attribute a
    WHERE
        a.attrelid = 'tracking'::regclass
        AND a.attnum > 0
        AND NOT a.attisdropped
    ORDER BY
        a.attnum;
    """

    return pd.read_sql(query, engine)
