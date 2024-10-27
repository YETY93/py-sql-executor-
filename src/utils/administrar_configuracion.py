import os
import pickle
from enum import Enum

from src.comun import constantes
from src.comun.ambientes_enum import Ambientes
from src.models.configuracion import Configuracion
from src.utils.crearcion_archivos import crear_dirtectorio
from src.utils.utils import existe_ruta





def guardar_ambiente(path_directorio: str, nombre_archivo_ambiente: str, config: Configuracion) -> bool:
    ruta_archivo: str = os.path.join(path_directorio, nombre_archivo_ambiente)

    try:
        crear_dirtectorio(path_directorio)

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

def persistir_configuracion_ambiente(ambiente: str, config: Configuracion):
    ruta_configuraciones: str = constantes.path_ambientes
    nombre_archivo: Enum = Ambientes.obtener_valor(ambiente)
    try:
         guardar_ambiente(ruta_configuraciones, nombre_archivo.value, config)
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None
