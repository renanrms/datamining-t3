import geopandas as gpd


def fetch_bus_data(connection, linha=None, limit=None):
    query = f"""
    SELECT
        ordem,
        geom,
        velocidade,
        datahora,
        datahoraservidor
    FROM tracking
        {f"WHERE linha = '{linha}' AND" if linha else ''}
        EXTRACT(HOUR FROM datahoraservidor) BETWEEN 8 AND 22
    ORDER BY datahoraservidor
    {f'LIMIT {limit}' if limit else ''}
    """

    # print(f"Executando consulta: {query}")

    try:
        # Usar geopandas para ler diretamente do PostGIS
        gdf = gpd.GeoDataFrame.from_postgis(query, connection, geom_col='geom')
        return gdf
    except Exception as e:
        print(f"Erro na consulta: {e}")
        return None
