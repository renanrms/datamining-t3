from sqlalchemy import create_engine

# Substitua pelos seus dados de conexão
engine = create_engine(
    "postgresql+psycopg2://postgres:example@localhost:5432/datamining-t3")
