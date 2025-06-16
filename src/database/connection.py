import psycopg2


connection = psycopg2.connect(
    dbname="datamining-t3",
    user="postgres",
    password="example",
    host="localhost"
)
