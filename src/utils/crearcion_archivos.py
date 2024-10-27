import os

from src.comun.constantes import path_sql


def crear_dirtectorio(path_directorio: str)-> bool:
    try:
        crear_directorio_sql()
        if not os.path.exists(path_directorio):
            os.makedirs(path_directorio)
            return True
    except OSError as e:
        print(f"No se ha podido crear el directorio '{path_directorio}'. Error: {e}")
        return False

def crear_directorio_sql():
    archivo_configuracion = os.path.join(path_sql, "configScripts.txt")
    try:
        if os.path.exists(archivo_configuracion):
            return
        os.makedirs(path_sql, exist_ok=True)
        with open(archivo_configuracion, "w") as file:
            pass
    except OSError as e:
        print(f"No se ha podido crear el directorio '{path_sql}'. Error: {e}")

