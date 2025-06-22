from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
from IPython.display import Image


def save_folium_as_png(mapa, file_path='mapa.png', delay=3):
    """
    Salva um mapa Folium como imagem PNG

    Parâmetros:
    mapa (folium.Map): Mapa a ser exportado
    file_path (str): Caminho para salvar a imagem
    delay (int): Tempo de espera para renderização (segundos)
    """
    # Salvar mapa como HTML temporário
    tmp_html = 'temp_map.html'
    mapa.save(tmp_html)

    # Configurar o navegador headless
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280x720')

    driver = webdriver.Chrome(options=options)
    driver.get(f'file://{os.path.abspath(tmp_html)}')

    # Esperar o mapa carregar
    time.sleep(delay)

    # Salvar screenshot
    driver.save_screenshot(file_path)
    driver.quit()

    # Remover arquivo temporário
    os.remove(tmp_html)

    return file_path
