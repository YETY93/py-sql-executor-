import os


def obtener_ruta_actual() -> str:
    """
    Obtiene la ruta del directorio de trabajo actual.

    Returns:
        str: La ruta del directorio actual.
    """
    return os.getcwd()


def existe_ruta(ruta: str) -> bool:
    """
    Verifica si una ruta específica existe en el sistema de archivos.

    Args:
        ruta (str): La ruta que se desea verificar.

    Returns:
        bool: True si la ruta existe, False en caso contrario.
    """
    return os.path.exists(ruta)


def existe_archivo(ruta: str) -> bool:
    """
    Verifica si un archivo específico existe en la ruta dada.

    Args:
        ruta (str): La ruta del archivo que se desea verificar.

    Returns:
        bool: True si el archivo existe, False en caso contrario.
    """
    return os.path.isfile(ruta)

