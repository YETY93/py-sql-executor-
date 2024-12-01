import os

from src.config.script_csv.configuracion_directorio_csv import (
    crear_directorio_csv,
)
from src.config.script_sql.configuracion_directorio_sql import (
    crear_directorio_sql,
)


def crear_dirtectorios(path_directorio: str)-> bool:
    try:
        crear_directorio_csv()
        crear_directorio_sql()
        if not os.path.exists(path_directorio):
            os.makedirs(path_directorio)
            return True
    except OSError as e:
        print(f"No se ha podido crear el directorio '{path_directorio}'. Error: {e}")
        return False
