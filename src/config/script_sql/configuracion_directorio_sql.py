
from src.comun.constantes import (
    EXTENSION_SQL,
    PATH_SQL,
    SCRIPT_INICIAL_NOMBRE_SQL,
    SCRIPT_INICIAL_SQL,
)
from src.utils.crear_archivos_util import crear_archivo


def crear_directorio_sql():
    try:
        crear_archivo(PATH_SQL, SCRIPT_INICIAL_NOMBRE_SQL, EXTENSION_SQL, SCRIPT_INICIAL_SQL, 'x')
    except OSError as e:
        print(f"No se ha podido crear el directorio '{PATH_SQL}'. Error: {e}")




