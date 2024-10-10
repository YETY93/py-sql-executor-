import os
import pickle

from src.models.configuracion import Configuracion
from src.utils.utils import existe_ruta


def crear_dirtectorio_base(path_directorio: str)-> bool:
    try:
        if not os.path.exists(path_directorio):
            os.makedirs(path_directorio)
            return True
    except OSError as e:
        print(f"No se ha podido crear el directorio '{path_directorio}'. Error: {e}")
        return False


def guardar_ambiente(path_directorio: str, nombre_archivo_ambiente: str, config: Configuracion) -> bool:
    ruta_archivo: str = os.path.join(path_directorio, nombre_archivo_ambiente)

    try:
        if not existe_ruta(path_directorio):
            crear_dirtectorio_base(path_directorio)
        with open(ruta_archivo, 'wb') as archivo:
            pickle.dump(config, archivo)
        ruta_absoluta = os.path.abspath(ruta_archivo)
        print(f"Se ha guardado el ambiente en '{ruta_absoluta}'")
        return True
    except IOError as e:
        print(f"Error al guardar el ambiente '{nombre_archivo_ambiente}'. Error: {e}")
        return False


def cargar_ambiente(path_directorio: str, nombre_archivo_ambiente: str) -> Configuracion | None:
    ruta_archivo: str = os.path.join(path_directorio, nombre_archivo_ambiente)
    try:
        with open(ruta_archivo, 'rb') as archivo:
            return pickle.load(archivo)
    except (IOError, pickle.UnpicklingError) as e:
        print(f"Error al cargar el ambiente '{nombre_archivo_ambiente}'. Error: {e}")
        return None

