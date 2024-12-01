from src.comun.constantes import (
    CABECERA_FORMAT_CSV,
    EXTENSION_CSV,
    INICIAL_NOMBRE_CSV,
    PATH_CONFIG_CSV,
)
from src.utils.crear_archivos_util import crear_archivo


def crear_directorio_csv():
    try:
        crear_archivo(PATH_CONFIG_CSV, INICIAL_NOMBRE_CSV, EXTENSION_CSV, CABECERA_FORMAT_CSV, 'x')
    except OSError as e:
        print(f"No se ha podido crear el directorio '{PATH_CONFIG_CSV}'. Error: {e}")




