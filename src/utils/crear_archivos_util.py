import os


def crear_archivo(path: str, nombre_archivo: str, extension: str,
                  contenido: str = None, permiso: str = 'w'):
    archivo_completo = os.path.join(path, nombre_archivo + extension)
    try:
        os.makedirs(os.path.dirname(archivo_completo), exist_ok=True)
        with open(archivo_completo, mode=permiso, encoding='utf-8') as archivo:
            if contenido:
                archivo.write(contenido)
    except OSError as e:
        print(f"No se ha podido crear el archivo '{archivo_completo}'. Error: {e}")
