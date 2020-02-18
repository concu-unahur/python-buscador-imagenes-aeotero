import logging
from api import PixabayAPI

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

carpeta_imagenes = './imagenes'
query = 'vehiculo militar'
api = PixabayAPI('15310851-8beba4d80305d85650c9c7cc2', carpeta_imagenes)

logging.info(f'Buscando imagenes de {query}')
urls = api.buscar_imagenes(query, 5)

for u in urls:
  logging.info(f'Descargando {u}')
  api.descargar_imagen(u)
