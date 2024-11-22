import os
import pickle
from enum import Enum

from src.comun import constantes
from src.comun.enums import ambientes_enum
from src.comun.enums.ambientes_enum import Ambiente_enum
from src.models.configuracion_model import Configuracion
from src.config.creacion_directorios import crear_dirtectorios


def guardar_ambiente(path_directorio: str, nombre_archivo_ambiente: str, config: Configuracion) -> bool:
    ruta_archivo: str = os.path.join(path_directorio, nombre_archivo_ambiente)
    try:
        crear_dirtectorios(path_directorio)
        with open(ruta_archivo, 'wb') as archivo:
            pickle.dump(config, archivo)
        ruta_absoluta = os.path.abspath(ruta_archivo)
        print(f"Se ha guardado el ambiente en '{ruta_absoluta}'")
        return True
    except IOError as e:
        print(f"Error al guardar el ambiente '{nombre_archivo_ambiente}'. Error: {e}")
        return False


def cargar_ambiente(path_directorio: str, nombre_archivo_ambiente: str) -> Configuracion | None:
    ambiente: Enum = Ambiente_enum.obtener_valor(nombre_archivo_ambiente)
    ruta_archivo: str = os.path.join(path_directorio, ambiente.value)
    try:
        with open(ruta_archivo, 'rb') as archivo:
            return pickle.load(archivo)
    except (IOError, pickle.UnpicklingError) as e:
        print(f"Error al cargar el ambiente '{nombre_archivo_ambiente}'. Error: {e}")
        return None


def persistir_configuracion_ambiente(ambiente: str, config: Configuracion):
    ruta_configuraciones: str = constantes.path_ambientes
    nombre_archivo: Enum = Ambiente_enum.obtener_valor(ambiente)
    try:
         guardar_ambiente(ruta_configuraciones, nombre_archivo.value, config)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None
