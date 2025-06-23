import geopandas as gpd


def fetch_bus_data(connection, linha=None, hour_range: tuple[int, int] = (8, 20), require_no_stopped=False, limit=None):
    query = f"""
    SELECT
        ordem,
        geom,
        velocidade,
        datahora,
        datahoraservidor
    FROM tracking
        {f"WHERE linha = '{linha}' AND" if linha else ''}
        {f"EXTRACT(HOUR FROM datahoraservidor) BETWEEN {hour_range[0]} AND {hour_range[1]}"}
        {"AND velocidade > 0" if require_no_stopped else ''}
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
