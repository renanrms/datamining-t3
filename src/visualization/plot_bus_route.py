import folium


def plot_bus_route(gdf):
    """
    Plota os pontos de trajeto no mapa sem clusterização

    Parâmetros:
    gdf (GeoDataFrame): DataFrame geoespacial com os dados

    Retorna:
    folium.Map: Objeto de mapa interativo
    """
    if gdf is None or gdf.empty:
        print("Nenhum dado encontrado para visualização")
        return None

    # Criar mapa centrado na média das coordenadas
    avg_lat = gdf["geom"].y.mean()
    avg_lon = gdf["geom"].x.mean()
    m = folium.Map(
        location=[avg_lat, avg_lon],
        zoom_start=13,
        tiles='OpenStreetMap',
        control_scale=True
    )

    # Adicionar controle de camadas
    folium.LayerControl().add_to(m)

    # Adicionar cada ponto ao mapa individualmente
    for idx, row in gdf.iterrows():
        popup_text = f"""
        <b>Veículo:</b> {row['ordem']}<br>
        <b>Data/Hora:</b> {row['datahoraservidor']}<br>
        <b>Velocidade:</b> {row['velocidade']:.1f} km/h
        """

        # Cor baseada na velocidade (opcional)
        speed = row['velocidade'] if 'velocidade' in row and row['velocidade'] else 0
        color = 'blue' if speed > 50 else 'green' if speed > 10 else 'yellow' if speed > 0 else 'red'

        folium.Circle(
            location=[row["geom"].y, row["geom"].x],
            radius=10,  # Tamanho do ponto em metros
            # popup=popup_text,
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.5,
            # tooltip=f"Veículo {row['ordem']}"
        ).add_to(m)

    # Adicionar título
    title_html = '''
    <h3 align="center" style="font-size:16px"><b>Trajeto de Ônibus</b></h3>
    <p align="center">Total de pontos: {}</p>
    '''.format(len(gdf))
    m.get_root().html.add_child(folium.Element(title_html))

    return m
